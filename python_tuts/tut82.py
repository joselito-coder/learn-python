import json

data = '{"var1":"harry","var2":50}'
print(data)

parsed = json.loads(data)

print(parsed['var1'])

# Task 1 - json.load
# --> json.load function parses a json by using a file pointer to the json file and converts it to a dict
# --> json.load() yeah function ek file se json ko convert karta hai dictionary meh

# Task 1
# json.load() --> yeah function ek file se json ko convert karta hai dictionary meh
# Task 2
# What is sort_keys parameter in dumps
# -> sort_keys parameter ek dict ke keys ko alphabetically sort karta hai json me convert karne se pehle

# jsonFile = open('misc_files/test.json')
# parsed = json.load(jsonFile)
# jsonFile.close()
# print(parsed)

data2 = {
    "channel_name":"CodewithHarry",
    "cars" : ['bmw','audi a8','ferrari'],
    "fridge": ('roti',540),
    "isbad":False
}

jscomp = json.dumps(data2)
print(jscomp)