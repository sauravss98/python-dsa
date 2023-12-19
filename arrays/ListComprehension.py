# list1 = [1,2,3,4]
# list2 = [item*2 for item in list1]
# print(list1)
# print(list2)

# list11 = [-1,10,-4,-5,5,6,3,-5]
# new_list = [number for number in list11 if number>0]
# print(list11)
# print(new_list)

# neg_list = [number*number for number in list11 if number<0]
# print(list11)
# print(neg_list)

# arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list3[1]= 'Kiwi'

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1]=='Kiwi':
#         sum+=20

# print(sum)

# data = [[[1,2],[3,4]],[[5,6],[7,8]]]
# def fun(m):
#     v = m[0][0]

#     for row in m:
#         print(row)
#         for element in row:
#             print(element)
#             if v < element : v = element
    
#     return v
# print(fun(data[0]))

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i],end= " ")

# def f(value,values):
#     v = 1
#     values[0] = 44

# t = 3
# v = [1,2,3]
# f(t,v)
# print(t,v[0])

# a= [1,2,3,4,5,6,7,8,9]
# print(a[::2])

# a= [1,2,3,4,5]
# print(a[3:0:-1])
# import random


# fruit = ['apple','banana','papaya','cherry']
# print(fruit)
# random.shuffle(fruit)
# print(fruit)

# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a)

class Solution:
    def twoSum(nums, target):
        seen = {}
        for i,value in enumerate(nums):
            print(f"seenm{seen}")
            print(f"value {value}")
            print(f"i {i}")
            complement = target - value
            print(f"complement{complement}")

            if complement in seen:
                print(f"complement{complement}")
                print(f"seen complement{seen[complement]}")
                print(f"i{i}")
                return[seen[complement],i]
            print(f"outer {i}")
            seen[value]= i
            print("----------------------------------------")
nums = [2,11,7,15]
target = 9
indices = Solution.twoSum(nums,target)
print(f"final {indices}")