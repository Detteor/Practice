import arcpy
import os
from glob import glob

workingPath = 'Q:\\GEO_PROJECT\\sp_TEST\\'

if not os.path.exists(workingPath + 'master.txt'):
    print('Master file not found, creating.')
    path = workingPath + "01_to_09_00\\*\\*\\*\\*\\*.*"
    actualPath = glob(path)
    txtFile = open(workingPath + 'master.txt', 'w')
    for row in actualPath:
        txtFile.write('%s\n' % row)
    txtFile.close()
elif os.path.exists(workingPath + 'master.txt'):
    print('Master file found, reading.')
    txtFile = open(workingPath + 'master.txt', 'r')
    actualPath = []
    for row in txtFile:
        actualPath.append(row[:-1])

urlDict = {}

print('Generating URL Links')
for row in actualPath:
    parcel = row[43:61].replace(' ', '-') + '-00001'
    url = 'SOME URL HEADER' + '\\INSPECTION_REPORTS' + row[34:]
    urlDict.update({parcel: url})

arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = True
#Change to work with local directories
engSDE = "path to engineering sde"
prodSDE = "path to production sde"

#Define Variables
#CLN = engSDE + '\\Engineering.DBO.Sewer\\Engineering.DBO.CLN'
CLN = 'C:\\TF\\PythonManuals\\Scripts\\temp\\Parcel_CLN_Join.shp'
#idFieldA = 'TieLateralHyperlink'
idFieldA = 'TieLater_1'
idFieldB = 'ParcelID'

print('Updating CLNs with Tie Lat Links')
with arcpy.da.UpdateCursor(CLN, [idFieldA, idFieldB]) as cursor:
    for row in cursor:
        if row[1] in urlDict:
            if row[0] == None or row[0] == '' or row[0] == ' ':
                print('Updating:' + row[1])
                row[0] = urlDict[row[1]].encode('utf8')
                cursor.updateRow(row)

