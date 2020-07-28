import arcpy as arc 
from arcpy import env
from arcpy import da

env.workspace = "C:/EsriTraining/PythonGP10_0/Data/SanJuan.gdb"
env.overwriteOutput = True

#set parameters used to join the BufferDistance table to the Roads feature class
inFeatures = "Roads"
inField = "ROUTE_TYPE"
joinTable = "BufferDistance"
joinField = "ROUTE_TYPE"
#join table to feature class
arc.JoinField_management(inFeatures, inField, joinTable, joinField)
#set parameters used to buffer Roads Feature Class
outBuffers = "RoadBuffers"
buffField = "DISTANCE"
#Buffer the roads based on DISTANCE attribute
arc.Buffer_analysis(inFeatures, outBuffers, buffField, dissolve_option="ALL")
