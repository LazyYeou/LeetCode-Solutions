class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        using xor operator
        if there is twice number xor operator
        number will return 0
        """
        x = 0
        for i in nums:
            x ^= i

        return x

        
