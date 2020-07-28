import arcpy as arc
from arcpy import env

lakes = arc.GetParameterAsText(0)
streams = arc.GetParameterAsText(1)
output = arc.GetParameterAsText(2)

# add script wizard available in arcmap. Write and Test Script
# with hard values to make sure it works. Then allow dynamic input
# like above. Create new toolbox for the script to be place in.
# Use script wizard to create a name for the tool, to write a description, 
# browse to the script, and provide built-in validation for the script parameters.
 