class Solution(object):
    def isAnagram(self, s, t):
        
        d = {}
        if s == "" and t == "":
            return True
        
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
            if d[k] != 0:
                return False
        return True

s = Solution()
print(s.isAnagram("a", "ab"))