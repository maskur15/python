#Dictionary in python
ages = {"hasan":22,"maika":90,"zadar":83,"Rakib":29,1:['Robart',"zabir","saber"]}
print(ages["hasan"])
print(ages["Rakib"])
print(ages[1])
ages[8]="zahid"
ages[9]="sopown"
print(ages)
#check weather a key is in the dictionary or not
if "hasan" in ages:
    print("Name hasan exist in the dictionary")
print("rasel" in ages)
#get method to check
print(ages.get("Rakib"))
print(ages.get(93))