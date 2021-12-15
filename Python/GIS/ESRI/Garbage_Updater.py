import arcpy
import os
from arcpy import env
from arcpy import da
from dotenv import find_dotenv, load_dotenv


import smtplib, os.path as op, base64, mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import  formatdate
from email import encoders

#Load Envs from env file
load_dotenv(find_dotenv())
work_email = "WORK_EMAIL"
email_server = "EMAIL_SERVER"
work_email_2 = "WORK_EMAIL_2"
database_user = "DB_USER_NAME"


env.overwriteOutput = True
env.qualifiedFieldNames = True
#change to work with local directories
engSDE = "user engineering sde connection"
prodSDE = "user production sde connection"

#Define Variables
A = prodSDE + "path to production"
idFieldA = 'Name'
B = engSDE + 'path to engineering'
idFieldB = 'PARCELID'
skip_Field = 'Multiple_Units'
notFound = []

print("Creating Dictionary")

#build dictionary with search cursor
geometries = {key:value for (key,value) in arcpy.da.SearchCursor(A, [idFieldA, 'SHAPE@'])}

#create edit session
edit = da.Editor(engSDE)
edit.startEditing(True, True)
edit.startOperation()

print("Update Starting...")

#Update B with geometries from A where IDs match
updatedParcels = []
with da.UpdateCursor(B, [idFieldB, skip_Field, 'SHAPE@']) as cursor:
    for row in cursor:
        if row[1] == '0':
            if row[2] != geometries[row[0]]:
                try:
                    print(row[0])
                    updatedParcels.append(row[0])
                    row[2] = geometries[row[0]]
                    cursor.updateRow(row)
                except:
                    notFound.append(row[0])
    print("Unable to update: ", notFound)

print("Update Finished. Reconciling and Posting.")

arcpy.ReconcileVersions_management(engSDE, 
                                 "ALL_VERSIONS", 
                                 "dbo.DEFAULT", 
                                 database_user, 
                                 "LOCK_ACQUIRED",
                                 "NO_ABORT",
                                 "BY_OBJECT",
                                 "FAVOR_TARGET_VERSION",
                                 "POST",
                                 "KEEP_VERSION",
                                 r"c:\Customer_Geo_Update.txt")

print("Posting Complete.")


if len(updatedParcels) > 0:
    print("Sending Email.")
    server = email_server
    sent_from = work_email
    sent_to = [work_email, work_email_2]
    subject = "Customer Garbage Parcel Updates"
    text = ""

    for item in updatedParcels:
        text = text + str(item) + "\n"
    text = text + "\nThank You"

    ## Use MIMEMultipart to build email
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = ", ".join(sent_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    ## Add Message Text
    message = MIMEBase('text', 'plain')
    message.set_payload(text)
    encoders.encode_base64(message)
    msg.attach(message)

    server = smtplib.SMTP(server)
    server.ehlo()
    ##server.starttls()
    server.sendmail(sent_from, sent_to, msg.as_string())
    server.quit()

    print("Email Sent!")

edit.stopOperation()
edit.stopEditing(True)
