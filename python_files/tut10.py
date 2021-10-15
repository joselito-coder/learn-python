# Dictionary is nothing but key value pairs
# d1= {}
# print(type(d1))

# Creating a dictionary
d2 = {
    "Harry":"Burger",
    "Rohan":"Fish",
    "SkillF":"Roti",
    "Shubam":{"B":"maggie","L":"roti","D":"chicken"}
}

# Adding to the dictionary
# d2["Ankit"] = "Junk food"
# d2[420] = "Kebab"
# print(d2)

# Removing from the dictionary
# del d2[420]
# print(d2["Shubam"]["D"])

# Copying a dictionary
# d3 = d2.copy()
# del d3["Harry"]
# print(d3 )
# print(d2)

# More functions
# print(d2.get("Harry"))
# d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())