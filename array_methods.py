import array

a = array.array('i',[2,2,3,4,5]) #Create Array 

def abc(array1):
    for i in array1:
        print(i)                #Traverse
    for i in range(len(array1)): #Print Index
        print(str(i)+ ':'+ str(a[i]))


    array1.append(4)            #Add to Last
    array1.insert(0,3)          # Add to specific position
    array1.extend(array.array('i',[2])) #Merge 
    list1 = [10,20,30]          #List 
    array1.fromlist(list1)      #Add list into Array 
    array1.remove(10)           #Remove an element
    array1.pop()                #Remove last element 
    array1.reverse()            #Reverse Array 
    
    return array1

print(abc(a))                   #Print final Array 
print(a.index(20))              
print(a.buffer_info())
print(a.count(2))
print(a.tolist())

# Two D Array 
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

n_a = np.array([7,8,9])

matrix = np.append(matrix,[n_a],axis=0) 
matrix = np.delete(matrix,0,axis=1) 
print(matrix)

# #When to use array
#     - Store multiple variables of same data type 
#     - Random access - O(1)

# #  when to not
#     - Reserve memory and may not use in future
