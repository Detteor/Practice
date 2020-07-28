# case sensitive parts of python: 
# variable names, classes, functions, methods, and properties
# ways to loop in python: while, for, in, and range 

import arcpy as arc
from arcpy import env
#simple for loop
for lyr in arc.mapping.ListLayers(mxd):
    if lyr.name == lower("Streets"):
        lyr.visible = True
    if lyr.name == lower("Water"):
        lyr.showLabels = True









env.workspace = "C:/EsriTraining"