class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            x = target-nums[i]
            if x in hash:
                return[i, hash[x]]
            else:
                hash[nums[i]] = i
                    
        
        
