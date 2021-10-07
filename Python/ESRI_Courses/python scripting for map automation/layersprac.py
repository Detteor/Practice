import arcpy as arc
from arcpy import env

env.workspace = "C:/EsriTraining/MapScripting/Westerville.gdb"
#specify which mapping document you want
mxd = arc.mapping.MapDocument("C:/EsriTraining/MapScripting/Exercise2/Westerville.mxd")
#create list of data frame
df = arc.mapping.ListDataFrames(mxd) [0]

#create list of layers
lyr = arc.mapping.ListLayers(mxd, "", df)[0]

lyr.visible = True

print (lyr)

arc.RefreshActiveView()
arc.RefreshTOC()
