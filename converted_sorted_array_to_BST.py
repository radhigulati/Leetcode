# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        
    	mid = len(nums)/2

        if not nums:
        	return None
        else:
        	root = self.TreeNode(nums[mid])
        	root.left = self.sortedArrayToBST(nums[:mid])
        	root.right = self.sortedArrayToBST(nums[mid+1:])
        	return root