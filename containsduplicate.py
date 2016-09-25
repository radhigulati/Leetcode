#Given an array of integers, find if the array contains any duplicates. 
#Your function should return true if any value appears at least twice in 
#the array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):

    	unique = set()

    	if len(nums) <= 1:
    		return False

    	for n in nums:
    		if n in unique:
    			return True
    		else:
    			unique.add(n)
    	return False


s = Solution()
print (s.containsDuplicate([3,5,3,4]))


