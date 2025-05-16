class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)

        temp = 100
        while temp != 0:
            temp = max_num % min_num
            max_num = min_num
            min_num = temp
        return max_num
        
