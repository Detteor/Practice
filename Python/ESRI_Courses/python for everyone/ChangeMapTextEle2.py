#import modules
import arcpy

#set environment
mxd = arcpy.mapping.MapDocument("CURRENT")

#list map layout text elements
eleList = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")

#loop through list and find all text elements with "Polk County" title
for ele in eleList:
    if ele.text == "Polk County":
        ele.text = "Polk County, OR"

#refresh the active view
arcpy.RefreshActiveView()

print ("Script completed")