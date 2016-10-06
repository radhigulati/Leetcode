class Solution(object):
    def isAnagram(self, s, t):
        d = {}
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in t:
            if i not in d:
                 d[i] = 1
            else:
                d[i] -= 1
        for k in d:
            if k == 0:
                return True
            return False

s = Solution()
print(s.isAnagram("anagram", "nagaram"))