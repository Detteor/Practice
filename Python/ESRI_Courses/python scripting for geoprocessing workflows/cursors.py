import arcpy as arc
from arcpy import env 
from arcpy import da
# set the environment variable
env.workspace = "C:/EsriTraining/PythonGP10_0/Data/SanJuan.gdb"
#create cursor 
rows = da.InsertCursor("Plants")
#Creates a new row
row = rows.newRow()
#update the plant name field
row.PLANT_NAME = "Canada Thistle"
#add the new row to the table
rows.insertRow(row)

del rows 
del row
#can get the value of a row 
fieldVal = row.getValue("DISTANCE")
#can set value for a row
row.setValue("DISTANCE", "1000")
#set row value to null
row.setNull("DISTANCE")

#initiate the cursor for inserting
campsites = da.InsertCursor("campsites")
#create data to insert into table
pnt = arc.Point(242340, 4165468)
#specify new Row for the new data
newFeature = campsites.newRow()
# the field shape is the pnt value
newFeature.SHAPE = pnt
#the field map_ID is 93
newFeature.Map_ID = 93
#Finished the rows
campsites.insertRow(newFeature)

del campsites