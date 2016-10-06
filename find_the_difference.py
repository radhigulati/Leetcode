class Solution(object):
	def findTheDifference(self, s, t):
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
			if d[k] != 0:
				return k
		return True

s = Solution()
print(s.findTheDifference("abcd", "abcde"))