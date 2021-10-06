import arcpy as arc
from arcpy import env

#set the environment variables
env.workspace = "C:/EsriTraining/PythonGP10_0/Data/SanJuan.gdb"
env.overwriteOutput = True
#Create New Table
arc.CreateTable_management("C:/EsriTraining/PythonGP10_0/Data/SanJuan.gdb", "Buffer_Distance")
#Create new fields
arc.AddField_management("Buffer_Distance", "ROUTE_TYPE", "TEXT")
arc.AddField_management("Buffer_Distance", "DISTANCE", "SHORT")

rows = arc.InsertCursor("Buffer_Distance")

row = rows.newRow()
row.ROUTE_TYPE = "Primary"
row.DISTANCE = 2000
rows.insertRow (row)
del rows
del row

print ("Finished Inserting")