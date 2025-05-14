class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return(sum(range(0, len(nums) + 1))-sum(nums))
        

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets = set(nums)
        length = len(sets)
        for i in range(0, length + 1):
            if i not in sets:
                return i
            
        
