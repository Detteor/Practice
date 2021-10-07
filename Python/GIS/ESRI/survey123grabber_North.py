import arcgis
from datetime import date
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
gis_user = "GIS_USER"
gis_password = "GIS_PASSWORD"

agoLogin = arcgis.GIS(url=None,
                      username=gis_user,
                      password=gis_password)

meterDate = input("Enter the date of the Meter Run (XX/XX/XXXX): ")
month = meterDate[:2]
day = meterDate[3:5]
year = meterDate[6:10]

if int(month) not in list(range(1,13)):
    raise Exception("Invalid Month!")

if int(day) not in list(range(1,32)):
    raise Exception("Invalid Day!")

try: int(year)
except: raise Exception("Invalid Year!")

itemToDownload = agoLogin.content.get("6e4bcc172e844736ad1aa8505537aed4")
exportLoc = r"path to export location"
itemExportName = "North Meter Route " + month + "_" + day + "_" + year
exportParameters = {"layers": [ {"id" : 0, "where" : "CreationDate > '"+ meterDate + " 12:00:00 AM'"} ] }

itemToDownload.export(title=itemExportName,
                      export_format="Excel",
                      parameters=exportParameters,
                      wait=True)

searchForExportedItem = agoLogin.content.search(query=itemExportName)
exportedItemID = searchForExportedItem[0].id
getTheExportedItem = agoLogin.content.get(exportedItemID)

getTheExportedItem.download(save_path=exportLoc,
                            file_name="{}.xlsx".format(itemExportName))

getTheExportedItem.delete()
