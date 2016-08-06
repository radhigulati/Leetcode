class Solution(object):
    def rob(self, nums):
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
            
        length = len(nums)
        work = [nums[0]]
        work.append(max(nums[0],nums[1]))
        
        for i in range(2, length, 1):
            work.append(max(work[i-2] + nums[i], work[i-1]))
            
        return work[len(work)-1]

s = Solution()
print (s.rob([4,6,13,2]))