class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_copy = 0
        x = []
        new_array = []
        for i in digits:
            digits_copy = (digits_copy * 10) + i
        digits_copy += 1

        while digits_copy > 0:
            x.append(digits_copy % 10)
            digits_copy //= 10
        return x[::-1]
            
        
