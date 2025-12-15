# num = 5789
# n = abs(num)
# if n == 0:
#     print(1)
# else:
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     print(count)

# extraction of digits
num=5783
n=num
while n>0:
    last_digits=n%10
    print(last_digits, end=" ")
    n=n//10


