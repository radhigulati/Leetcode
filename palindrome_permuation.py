class Solution(object):
    def canPermutePalindrome(self, s):
        
        d = {}
        
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        count1 = 0
        
        for val in d:
            if d[val] % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True