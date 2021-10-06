import arcpy as arc
#Create list of feature classes to Buffer
bufferList = [arc.GetParameterAsText(0), arc.GetParameterAsText(1)]
#Get variables from the user
# Lakes = arc.GetParameterAsText(0)
#Initialize a new Python list of feature classes to be Unioned together
unionList = []
for fc in bufferList:
    #Buffer each feature class and dissolve any overlapping polygons
    arc.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "ALL")
    #Add each buffer feature class to a list of feature classes to Union
    unionList.append(fc + "Buffer")
#Union the buffered feature classes
arc.Union_analysis(unionList, arc.GetParameterAsText(2))
