# To find the factorial of a number
def func(n):
    if n==1:
        return 1
    return n*func(n-1)

print("Factorial Of number is: ",func(5))