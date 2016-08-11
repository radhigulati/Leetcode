class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, e in enumerate(num):
            k = target - e
            if k in d:
                return (d[k], i)
            d[e] = i


s = Solution()
print (s.twoSum([3,2,4],6))