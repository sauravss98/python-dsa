"""
Module for demonstrating array operations and basic algorithms.
"""

from array import array

# Define some array examples
arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 2.0])

def traverse_array(array_instance):
    """
    Traverse through the array and print each element.
    
    Args:
        array_instance (array): The array to traverse.
    """
    for element in array_instance:
        print(element)

def access_element(array_instance, index):
    """
    Access an element in the array by index.
    Prints a message if the index is out of range.
    
    Args:
        array_instance (array): The array to access.
        index (int): The index of the element to access.
    """
    if index >= len(array_instance):
        print("There is no element at this index.")
    else:
        print(array_instance[index])

def linear_search(arr, target):
    """
    Perform a linear search for the target in the array.
    
    Args:
        arr (array): The array to search in.
        target (int): The target value to search for.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Example usage of the functions
if __name__ == "__main__":
    print("Linear search for 5:", linear_search(arr1, 5))
    print("Linear search for 7:", linear_search(arr1, 7))
    arr1.remove(5)
    print("Array after removing 5:", arr1)
