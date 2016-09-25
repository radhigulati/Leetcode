"""
Problem: Given a sequence of nonnegative integers A and an integer T, return whether there is a *continuous sequence* of A that sums up to exactly T

Example
[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
[1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7

Note: We are looking for an O(N) solution. There is an obvious O(N^2) solution which is a good starting point but is not the final solution we are looking for.


class ContSum(object):
    def continuous(self, nums, target):
        if len(nums) == 0:
            return
        sum = 0
        next = 0
        
        for i in range(0, len(nums), 1):
            sum += nums[i]
            while sum > target:
                sum -= nums[next]
                next += 1
            if sum == target:
                return True
        return False
"""
class ContSum(object):
    def continuous(self, nums, target):
        if len(nums) == 0:
            return
        sum = 0
        start = 0
        begin = 0
        
        length = len(nums)
        
        while start < length:
            if sum == target:
                return True 
            elif sum < target:
                if begin < length:
                    sum += nums[begin]
                    begin += 1
                else:
                    return False
            else:
                # reset counter
                start += 1
                begin = start
                sum = 0
        if sum != target:
            return False
        else:
            return True 

s = ContSum()
print(s.continuous([1, 3, 5, 23, 2], 7))