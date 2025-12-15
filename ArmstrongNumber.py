# Armstrong number program
n=1534
num=n
node=len(str(n))
total=0
while n>0:
    id=n%10
    total=total+(id**node)
    n=n//10
if total==num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")