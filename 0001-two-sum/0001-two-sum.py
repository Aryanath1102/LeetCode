class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1,i2=0,0
        m= nums[0]+nums[1]
        c=nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    n=nums[i]+nums[j]
                    if nums[i]+nums[j]==target:
                        i1=i
                        i2=j
                  
                        break
        return [i1,i2]     