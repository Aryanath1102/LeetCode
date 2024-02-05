class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return 0
        f=0
        s=set(nums)
        l=[]
        for i in range (1,len(nums)):
            
            if i not in s:
                l.append(i)
        if len(nums) not in s:
            l.append(len(nums))
        return l