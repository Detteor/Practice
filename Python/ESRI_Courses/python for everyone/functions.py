#assigning variables strings
cen = "Census" 
parc = "Parcels"
parks = "Parks"
st = "Streets"
bound = "parksbound.shp"
lakes = "lakes.shp"
sch = "schools.shp"
riv = "Rivers.shp"

datalist = [cen, bound, parc, lakes, parks, sch, st, riv] #array of items

for item in datalist: 
    if item.endswith(".shp"): #specify which items are to be deleted
        datalist.remove(item) #remove the items within datalist from file

print datalist #see the results of datalist in the console
 
path = r"C:\Users\MKinnaman\Desktop\WestervilleUpdates.txt" #read file 

#common statements
# print 
# import
# del
# for in 
# if else 
# try except 

amount = 49
if amount >= 50:
        print ("Amount is great than or equal to 50")
else:
        print ("Amount is less than 50")

areaList = ["40000 feet", "23908 feet", "120000000 feet"]
for area in areaList:
        area.replace("feet", "meters")

country = "france"
if country == "italy":
        print ("This country is" + country)
elif country == "france":
        print ("This country is" + " " + country)
else:
        print ("This is not a country")

file = open(path, "w") #open file in write mode
for updItem in datalist: #create variable to write to file
    file.write(updItem + "\n") #write updItem, then make a new line

file = open(path, "r") #open file in read mode 

file.close() #close file when finished writing to it
 
len() #length of the object
open() #open a file
max() #finds the largest number inside a tuple or list 

#Methods
Country = "italy"
Country.capitalize() #capitalize the string

CountryList = ["Italy", "Germany", "UK", "France"]
CountryList.count() #count the string

species = "sparrow"
species.upper()


import math #import functions and classes
math.sqrt() #square root function
math.cos() #cosine function
math.exp() #exponents function
math.pow() #variable to x power function
 
