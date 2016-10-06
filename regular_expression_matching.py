class Solution(object):	
	def isMatch(self, s, p):
	    if p and s:
	        if p[0] == s[0] or p[0] == ".":
	            if len(p) > 1 and p[1] == '*':
	                return self.isMatch(s[1:], p)
	            return self.isMatch(s[1:], p[1:])
	        else:
	            if len(p) > 1 and p[1] == '*':
	                return self.isMatch(s, p[2:])                
	                
	    elif not p and not s:
	        return True
	        
	    elif p and not s:
	        if len(p) == 2 and p[1] == '*': return True


	    return False

test = Solution()
print(test.isMatch("aa","a"))
print(test.isMatch("aa","aa"))
print(test.isMatch("aaa","aa"))
print(test.isMatch("aa","a*"))
print(test.isMatch("aa",".*"))
print(test.isMatch("ab",".*"))
print(test.isMatch("aab","c*a*b"))
print(test.isMatch("ab",".*c"))