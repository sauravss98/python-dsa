"""
Module for performing a linear search.
"""

def linear_search(lst, target):
    """
    Perform a linear search on a list to find the target value.

    Args:
        lst (list): The list to search through.
        target (int): The target value to find.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    position = linear_search(lst, target)
    print(f"{target} found at position {position}")
