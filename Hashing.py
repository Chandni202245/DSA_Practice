# n=[1,2,5,3,4,5,5,5,2,10,6,7,7]
# m=[10,2,3,5,67,33,3]
# hash_list=[0]*11
# for num in n:
#     hash_list[num]+=1
# for num in m:
#     if num<0 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

# character hashing
"""s="azyxyyzaaaaABCC"
q=['d','a','y','x','A','C']
hash_list=[0]*128
for ch in s:
    index=ord(ch)
    hash_list[index]+=1
for ch in q:
    index=ord(ch)
    print(hash_list[index])
"""

# if only lowercase is available
"""s="azyxyyzaaaa"
q=['d','a','y','x']
hash_list=[0]*26
for ch in s:
    ascii_value=ord(ch)
    index=ascii_value-97
    hash_list[index]+=1
for ch in q:
    ascii_value=ord(ch)
    index=ascii_value-97
    print(hash_list[index])"""


# Dictionary Approach
s = "azyxyyzaaaaABCC"
q = ['d', 'a', 'y', 'x', 'A', 'C']
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in q:
    print(freq.get(ch,0))
