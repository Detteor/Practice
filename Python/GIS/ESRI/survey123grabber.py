import arcgis
from datetime import date
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
gis_user = "GIS_USER"
gis_password = "GIS_PASSWORD"

def grabSurvey123(meterDate, direction, exportLoc):
    print('Beginning ' + direction + ' Route Survey123 Download.')
    print('Logging into ArcGIS.')
    agoLogin = arcgis.GIS(url=None,
                          username= gis_user,
                          password= gis_password)

    month = meterDate[:2]
    day = meterDate[3:5]
    year = meterDate[6:10]

    featureID = ""
    if direction == "North":
        featureID = "6e4bcc172e844736ad1aa8505537aed4"
    if direction == "South":
        featureID = "22af1b6e3ff04c0497fc12b57692b0e8"

    itemToDownload = agoLogin.content.get(featureID)
    itemExportName = month + day
    exportParameters = {"layers": [ {"id" : 0, "where" : "CreationDate > '"+ meterDate + " 12:00:00 AM' AND CreationDate < '"+ meterDate + " 11:59:59 PM'"} ] }

    print('Generating Excel in ArcGIS Online.')
    itemToDownload.export(title=itemExportName,
                          export_format="Excel",
                          parameters=exportParameters,
                          wait=True)

    searchForExportedItem = agoLogin.content.search(query=itemExportName)
    exportedItemID = searchForExportedItem[0].id
    getTheExportedItem = agoLogin.content.get(exportedItemID)

    print('Downloading to: ' + exportLoc)
    getTheExportedItem.download(save_path=exportLoc,
                                file_name="{}.xlsx".format(itemExportName))

    print('Download Complete! Removing ArcGIS Online file.')
    getTheExportedItem.delete()

def downloadPictures(meterDate, direction, pictureLoc):
    print('Beginning ' + direction + ' Route Survey123 Image Download.')
    print('Logging into ArcGIS.')
    agoLogin = arcgis.GIS(url=None,
                          username=gis_user,
                          password=gis_password)
    
    featureID = ""
    if direction == "North":
        featureID = "6e4bcc172e844736ad1aa8505537aed4"
    if direction == "South":
        featureID = "22af1b6e3ff04c0497fc12b57692b0e8"

    myFLItem = agoLogin.content.get(featureID)
    attachmentsLayer = myFLItem.layers[0]
    oidField = attachmentsLayer.properties.objectIdField
    myRecords = attachmentsLayer.query(where="CreationDate > '"+ meterDate + " 12:00:00 AM' AND CreationDate < '"+ meterDate + " 11:59:59 PM'",out_fields=oidField)

    for r in myRecords.features:
        myOID = r.get_value(oidField)
        attachments = attachmentsLayer.attachments.get_list(myOID)
        for attachment in attachments:
            myDownload = attachmentsLayer.attachments.download(oid=myOID, attachment_id=attachment['id'],save_path=pictureLoc)
            print ("Downloaded:" + myDownload[0])
