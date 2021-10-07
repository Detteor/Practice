import arcpy as arc
#Set geoprocessing environment
arc.env.workspace = "C:\\EsriTraining\\PythonGP10_0\\Data\\SanJuan.gdb"
#boolean data type can also be 1 for true and 0 for false
arc.env.overwriteOutput = True

#Create list of feature classes in SanJuan
fcList = arc.ListFeatureClasses()

#Create a loop to buffer lakes and streams
bufferList = []
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arc.Buffer_analysis(fc, fc + "Buffer", "1000 meters", dissolve_option="ALL")
        bufferList.append(fc + "Buffer")

arc.Union_analysis(bufferList, "WaterBuffers")

waterBuffers = "WaterBuffers"

arc.Buffer_analysis(waterBuffers, "WaterBuffer", "1000 meters", dissolve_option="ALL")

print ("Union and dissolve Finished")

#after the union buffer it as well

