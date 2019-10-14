# Dictionaries
# dict
# not ordered

my_dictonary = {
    "key" : "value", 
    "key2" : "78"
}


product = {
    "id"            :86544665,
    "description"   :"auto taco maker",
    "price"         :19.99,
    "weight"        :9001,
    "department"    :"stuff",
    "aisle"         :3,
    "shelf"         :"B"
}


print(product["price"])

# location = (product["aisle"],product["shelf"])


# print(product.get("quantity")) # this is safe and will return "none" if the key word is not there

# # you can directly change things in a dictonary
# product["aisle"] = 4  
# product["aisle"] += 1
# product["dept"] = "Guy's Gocery games"

# for value in product:  # prints all keys
#     print(value)

# for value in product:  # prints all values in dictonary
#     print(product[value]) 


# print(product.values()) # will print a list of the values
# print(product.keys()) # will print a list of the values

# product.update({"whatever": 123456}) # this will add to the dictonary

# you={}

# data = [ ("name", "JimBo"),("age", 40), ("class", "Python")]


# for a , b in data:
#     you.update({a: b})
#     print(you.values(),you.keys()) # will print a list of the values
  

#   # best way to add info to a dictionay super slick

#     you.update(data)
#     print(you)