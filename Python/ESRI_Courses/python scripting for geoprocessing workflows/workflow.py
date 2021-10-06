#import arcpy 
#set environments
#create list of GIS objects
#Iterate through list elements, for-loop 
#execute geoprocessing

import arcpy as arc

arc.env.workspace = "C:/Data"
arc.env.overwriteOutput = True
arc.ResetEnvironments #resets all the environment values
arc.env.cellSize = 10
print (arc.ListEnvironments())

#checks the raster size to insure it is uniform
if arc.env.cellSize < 10:
    arc.env.cellSize = 10
elif arc.env.cellSize > 20:
    arc.env.cellSize = 20 

desc = arc.Describe(r"C:\EsriTraining\PythonGP10_0\Data\SanJuan.gdb\Lakes")

print desc.shapeType
print desc.spatialReference.Name

#properties of describe http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-functions/describe.htm

#Set the workspace environment
arc.env.workspace = r"C:\\EsriTraining\PythonGP10_0\Data\SanJuan.gdb"

#Access properties of the Roads feature class http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-functions/dataset-properties.htm
desc = arc.Describe("Roads")

#Create a Describe object from the Elevation raster dataset
desc = arc.Describe(r"C:\EsriTraining\PythonGP10_0\Data\Elevation.tif")

#Get the extent of the raster dataset http://desktop.arcgis.com/en/arcmap/latest/tools/environments/compression.htm
extent = desc.Extent

#Set the compression type for new rasters
arc.env.compression = "LZ77"

import arcpy as arc
#set the workspace. There is a difference between workspace and Workspace 
arc.env.workspace=r"C:\EsriTraining\PythonGP10_0\Data\SanJuan.gdb"
fcList = arc.ListFeatureClasses ()
#Creating list
ListDatasets #returns the datasets
ListFeatureClasses #returns the feature classes
ListFields # returns a list of attribute fields
ListRasters #returns a list of rasters
ListWorkspaces #returns a list of workspaces within the current workspace 

#for loop to show the spatial reference name for each class
for fc in fcList:
    desc = arc.Describe(fc)
    print desc.spatialReference.Name
