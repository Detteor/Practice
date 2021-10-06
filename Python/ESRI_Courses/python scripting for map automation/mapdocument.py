import arcpy as arc
from arcpy import env
#set the workspace environment
env.workspace = "C:\\EsriTraining\\MapScripting\\Westerville.gdb"

#identify the current mxd, used within arcmap
mxd = arc.mapping.MapDocument("CURRENT")
#use outside of arcmap
mxd = arc.mapping.MapDocument("C:/map/City.mxd")
#replace the current workspace with a geodatabase 
mxd.replaceWorkspaces(r"C:\Shapefiles", "SHAPEFILE_WORKSPACE", r"C:\Geodatabase", "FILEGDB_WORKSPACE")
mxd.saveACopy(r"C:\Geodatabase\Westerville_gdb.mxd")
del mxd

#you cannot create a map document with arcpy, but you can edit the features with arcpy.mapping
mxd.author = "GIS Department"
mxd.save()
#to release the mxd from memory and remove a possible lock on the file
del mxd 