import arcpy

buff500 = 500
buff1000 = 1000
buff2000 = 2000

buffList = [buff500, buff1000, buff2000]

for buff in buffList:
    arcpy.Buffer_analysis(#input layer, output feature class, buffer unit, full side type, round end type, dissolve none, blanks are the # sign
    "streets", "C:/Users/.gdb/Buff" + str(buff), buff, "FULL", "ROUND", "NONE", "#")

arcpy.Clip_analysis(in_features="RI_Schools", clip_features="Providence", out_feature_class="C:/EsriTraining/PythEveryone/PythonInArcGIS/RhodeIsland.gdb/Schools", cluster_tolerance="") #clip schools

#clip sewers
