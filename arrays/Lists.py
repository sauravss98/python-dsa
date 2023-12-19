list = [1,2,3,4,5,6,7,8,9]
def linear_search(list,target):
    for i,value in enumerate(list):  
        if value == target:
            return i
    return -1
target = 4
# value = linear_search(list,target)
print(f"{target} found in position {linear_search(list,target)}")