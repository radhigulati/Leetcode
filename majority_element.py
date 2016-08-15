import math
class Solution(object):
    def majorityElement(self, nums):
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for key,val in d.items():
            print(d)
            if val > math.floor(len(nums)/2):
                return key
        return key

s = Solution()
print(s.majorityElement([5,6,5]))