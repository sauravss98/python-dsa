"""
Module to find the sum and product of elements in an array.
"""

def product_sum(array_value):
    """
    Calculate the sum and product of elements in the given array.

    Args:
        array_value (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum and product of the array elements.
    """
    sum_of_array = 0
    product_of_array = 1

    for value in array_value:
        sum_of_array += value
        product_of_array *= value

    return sum_of_array, product_of_array

if __name__ == "__main__":
    array_value = [2, 4, 5, 6, 7]
    sum_result, product_result = product_sum(array_value)
    print(f"Sum = {sum_result}, Product = {product_result}")
