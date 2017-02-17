from pprint import pprint
#from the pprint module, import the pprint function
#Dictionary
#dictionaries contain key value pairs
d={
#    key  :  value
    "name":"Cecilia",
    "birthmonth":"January",
    "grade":10
}

print(d['name'])

schedule={
    "A":"English",
    "B":"Algebra",
    "C":"AP Chemistry",
    "D":"Global History"
}

schedule["F"]="SE9"
print(schedule["f"])


#Add a key-value pair where the key is "E" and
#the value is "holla"
schedule['E'] = "holla"
print(schedule['E'])

#only checks if it exists as a key NOT a value

if "E" in schedule:
    print("is in schedule")
else:
    print("is not in schedule")
    
#how to check if a value exists?
for key in schedule:
    if schedule[key] == "SE12":
        print("Exists as value!")
        break
    else: #This only happens if for loop doesn't break
        print("does not exist as value!")