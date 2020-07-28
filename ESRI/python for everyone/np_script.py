import arcpy 

parks = r""
ecoreg = r""
parkEco_int = r""

try: 
    if arcpy.Exists(parkEco_int):
        arcpy.DeleteFeatures_management(parkEco_int)

    else: print parkEco_int + " does not already exist"

    arcpy.Intersect_analysis([parks,ecoreg], parkEco_int)

    print ("Script Completed")

except: 
    print ()