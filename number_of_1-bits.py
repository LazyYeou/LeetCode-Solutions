class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_array = []
        sum = 0

        while n > 0:
            if n % 2 == 0:
                binary_array.append(0)
            else:
                binary_array.append(1)
            n //= 2
        for i in binary_array:
            sum += i
        return sum    
        

        '''
        128 => 64, 32, 16, 8, 4, 2 , 1
            => 0, 0, 0, 0, 0,0,0,1
        '''
        
