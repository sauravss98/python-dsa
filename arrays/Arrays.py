from array import *


# my_array = array.array('i')
# print(my_array)
# my_array1 = array.array('i',[1,2,3,4])
# print(my_array1)

arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,1.5,2.0])
# my_array1.insert(0,6)
# print(my_array1)

def traverseArray(array):
    for i in array:
        print(i)

# traverseArray(arr1)

def accessElement(array,index):
    if index>len(array):
        print("There is not any element in this index")
    else:
        print(array[index])

# accessElement(arr1,2)
# accessElement(arr1,10)
        
def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(linearSearch(arr1,5))
print(linearSearch(arr1,7))

arr1.remove(5)
print(arr1)

# import numpy as np

# np_array = np.array([],dtype=int)
# print(np_array)
# np_array1 = np.array([1,2,3,4,5],dtype=int)
# print(np_array1)

