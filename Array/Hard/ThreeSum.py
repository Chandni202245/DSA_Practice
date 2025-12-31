# Optimal Solution
from typing import List
class Solution:
    def threeSum(self,nums: List[int])->List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            # moving the 2 pointers
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1

                    # skip the duplicates if occurred
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans
    
arr=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]

sol = Solution()
result = sol.threeSum(arr)
print(result)

# Time Complexity: O(n log n) +O(n^2)
# Space Complexity: O(1)   (ignoring output list)
