def ProductSum(array):
    sum=0
    product = 1
    for i in array:
        sum+=i
        product*=i
    print(f"Sum = {sum}, Product = {product}")

array = [2,4,5,6,7]
ProductSum(array)