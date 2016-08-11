# Given an array of integers, every element appears 
# twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        
        d = {}

        for i in nums:
        	if i in d:
        		d[i] += 1
        	else:
        		d[i] = 1

        for k in d:
        	if d[k] < 2:
        		return k

s = Solution()
print (s.singleNumber([1,1,2,2,3]))
