import operator
class Solution(object):

	def calculate_word_frequency(self,s):
		words = s.split()
		freq = {}
		for word in words:
			if word in freq:
				freq[word] += 1
			else:
				freq[word] = 1
		return freq

s = Solution()
print(s.calculate_word_frequency("abc def-ghi jkl abc"))