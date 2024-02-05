class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=Counter(nums)
        
        for i in l.elements():
            if l[i]==1:
                return i
        
