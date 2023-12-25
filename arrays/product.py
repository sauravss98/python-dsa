"""
Finds product and the sum
"""
def product_sum(array_value):
    """
    Finds product and the sum
    """
    sum_of_array=0
    product_of_array = 1
    for i in array_value:
        sum_of_array+=i
        product_of_array*=i
    print(f"Sum = {sum_of_array}, Product = {product_of_array}")

array_value = [2,4,5,6,7]
product_sum(array_value)
