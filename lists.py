lists = [1,2,3,4,5]
lists.insert(1,10)
lists.append(10)
lists.pop()
del lists[0]
lists.remove(5)
list2 = [1]

lists.extend(list2)
print(lists[0:2])
print(lists)

# Concentae 
a = [1]
b = [2]
c = a+b
c = c * 4
print(c)
print(len(c))
print(max(c))
print(min(c))
print(sum(c))

# Strings
d = "Hello World"
e = list(d)    #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
f = d.split()  #['Hello', 'World']
print(f)

# Note - In operator has a better time complexity when used with sets and dictionary which are implemented as hash tables
#  Hashtable is a way of doing key value lookups. 
#  key -> Hash -> Calculate Index and store value in that index 

#Drawbacks of Lists 
#Most of the lists, do the operation and return none 

##Arrays vs Lists 

# Similarities - Mutable, Indexed, Sliced
# Arrays are for arthmetic ops
# Lists can hold diff data types 

## Dictionaries vs List 
# Unordered - Ordered
# (Became ordered from 3.7)
# Access Keys     Index
# Key Value       elements
# unique key      ordered data
# No duplicate    duplicate allowed 



