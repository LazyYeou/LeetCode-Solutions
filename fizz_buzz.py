class Solution(object):
    def fizzBuzz(self, n):
        return [self.get_str(x) for x in range(1, n+1)]
        
    def get_str(self, x):
        f = "Fizz"
        b = "Buzz"
        ans = ''
        if x % 3 == 0:
            ans += f
        if x % 5 == 0:
            ans += b
        return str(x) if len(ans) == 0 else ans

                
        
