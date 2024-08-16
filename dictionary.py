# Creating a dictionary same as Object in JS
my_dict = {
    "key1": "texts",
    "key2": "value2",
    (1, 2): "value"
}

# Accessing values
value1 = my_dict["key1"]

print(value1)

# Adding a new key-value pair
my_dict["key3"] = "value3"

# Checking if a key exists
if "key1" in my_dict:
    print("Key1 exists")

keys = my_dict.keys()

for key, value in my_dict.items():
    print(key, value)


print(keys)


