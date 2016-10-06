class Solution(object):
    def firstUniqChar(self, s):
    	d = {}

    	for i in s:
    		if i not in d:
    			d[i] = 1
    		else:
    			d[i] += 1

    	for i,j in enumerate(s):
    		if d[j] == 1:
    			return i
    		else:
    			i += 1
    	return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))