# Given an integer n, calculate the sum of series 1^3 + 2^3 + 3^3 + ^43 + … till n-th term.
def func(n):
    if n==0:
        return 0
    return (n**3)+func(n-1)
print(func(5))