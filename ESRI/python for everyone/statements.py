amount = 49 
if amount >=50: 
    print ("Amount is greater than or equal to 50")
else: 
    print("Amount is less than 50")

AreaList = ["40000000 feet", "23908 feet", "1200000000 feet"]
for area in AreaList:
     area.replace("feet", "meters")
print(area)

Country = "italy"
if Country == "italy": 
     Country.capitalize()
     Country.center()
else: 
     print ("This country will not be capitalized.")