import arcpy as arc

from arcpy import env

#set the environment to work in
env.workspace = "C:/EsriTraining/MapScripting/Westerville.gdb"
#set mxd variable to map document
mxd = arc.mapping.MapDocument("C:/EsriTraining/MapScripting/Exercise2/Westerville.mxd")
#change workspace from personal gdb to regular gdb
mxd.replaceWorkspaces("C:/EsriTraining/MapScripting/City_of_Westerville.mdb", "ACCESS_WORKSPACE", "C:/EsriTraining/MapScripting/Westerville.gdb", "FILEGDB_WORKSPACE")
#save a copy of the new mxd
mxd.saveACopy("C:/EsriTraining/MapScripting/Westerville_update.mxd")
#cleanup temporary files created
del mxd 
