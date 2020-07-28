import arcpy as arc
from arcpy import env
from arcpy import da
#setup the environment
env.workspace = "C:/EsriTraining/PythonGP10_0/Data/SanJuan.gdb"
env.overwriteOutput = True
#List for processing of fc
treatmentList = ["RoadBuffers", "WaterBuffers"]
#Union of feature classes
arc.Union_analysis(treatmentList, "NonChemical")
print ("Union Finished")
#need to create temp layer before processing due to selectlayerbylocation not able to use FC
arc.MakeFeatureLayer_management("Invasive_Plants", "Invasive_Plants_lyr")
#Select invasive species within streams and lakes
arc.SelectLayerByLocation_management("Invasive_Plants_lyr", "INTERSECT", "NonChemical")
print ("Selection Finished")
#add field for calculation
arc.AddField_management("Invasive_Plants", "TREATMENT", "TEXT")
#calculate new field called treatment in invasive plants layer and fill in the field with non-chemical if within the select layer by location
arc.CalculateField_management("Invasive_Plants","TREATMENT",'"NON-CHEMICAL"')
print ("Calculation Finished")

print ("Finished")
