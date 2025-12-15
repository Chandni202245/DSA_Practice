# Head Recursion

"""def func(i,n):
    # base case
    if i>n:
        return 
    print(i)
    # Recursive call
    func(i+1,n)
# function call
func(1,4)"""

# Tail Recursion / Backtracking

# print name N times using tail recursion

def func(count,n):
    if count==n:
        return
    func(count+1,n)
    print("Chandni")

func(0,4)