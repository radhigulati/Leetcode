class Solution(object):
	def isPalindrome(self, input):
			pointer1 = 0
			pointer2 = len(input)-1

			while (pointer1 < pointer2):
				if input[pointer1] != input[pointer2]:
					return False
				pointer1 += 1
				pointer2 -= 1
			return True

s = Solution()
print(s.isPalindrome(''))