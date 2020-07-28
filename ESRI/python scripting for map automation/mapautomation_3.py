#use arcpy.mp for python 3

import arcpy as arc
#selecting a project instead of a mxd
p = arc.mp.ArcGISProject("CURRENT")

m = p.listMaps("City of Dallas")[0]

for lyr in m.listLayers():
    if lyr.supports("SHOWLABELS"):
        lblClasses = lyr.listLableClasses()


aprx = arc.mp.ArcGISProject(r"C:\Projects\blank.aprx")
aprx.importDocument(r"C:\Projects\YosemiteNP\Documents\Yosemite.mxd")
aprx.importDocument(r"C:\Projects\YosemiteNP\Documents\Yosemite_ScenicViews.3dd")
aprx.defaultToolGeoDatabase = r"C:\Projects\YosemiteNP\Data_Vector\YosemiteData.gdb"
aprx.defaultToolbox = r"C:\Projects\YosemiteNP\Analysis\AnalysisTools.tbx"
aprx.saveACopy(r"C:\Projects\YosemiteNP\Yosemite.aprx")

lf = arc.mp.LayerFile(r"C:\Projects.lyrx")
lf.listLayers.listLableClasses()

