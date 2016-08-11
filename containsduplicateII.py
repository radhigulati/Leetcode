#Given an array of integers and an integer k, 
#find out whether there are two distinct indices 
#i and j in the array such that nums[i] = nums[j] 
#and the difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

    	d = {}
    	for i, e in enumerate(nums):
    		print ("i,e",i,e)
    		if e in d:
    			print ("e", e)
    			print ("d", d)
    			print ("i",i)
    			print ("d[e]", d[e])
    			if i - d[e] <= k:
    				print ("i-d[e]", i - d[e])
    				return True
    		d[e] = i
    		print ("d[e]",d[e])
    	return False

s = Solution()
print (s.containsNearbyDuplicate([2,3,2,4,4,5],1))
