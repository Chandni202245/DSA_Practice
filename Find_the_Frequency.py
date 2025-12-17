"""Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :
Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5"""

def func(arr,x):
    count=0
    for i in arr:
        if i==x:
            count+=1
    return count

arr=[1,2,2,2,4,5,2]
print("Number of frequency of number is: ",func(arr,2))