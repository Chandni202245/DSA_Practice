num=51151
n=num
revers=0
while n>0:
    last_digits=n%10
    revers=(revers*10)+last_digits
    n=n//10
if revers==num:
    print("its a palindrome number")
else:
    print("it is not a palindrome")

