

a = {
    "hi": 1
}
a['hi'] = 3 #O(1)
a['hii']=1 #O(1)
a['hello'] = 3

def dictin(d):
    for i in d:
        print(i,d[i])

dictin(a)

del a['hi'] #O(1)
a.pop('hii')
a.popitem() #Last element 
a.clear() #Clean O(n)
b = a.copy()
c = {}.fromkeys([1,4,3],0)
print(c.get(1,2)) 
print(c.setdefault(1,2)) 
print(c.items())
print(c.keys())
print(c.values())
print(1 not in c.values())
print(len(c))
print(sorted(c))

