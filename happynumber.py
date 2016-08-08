class Solution(object):
	def happyNumber(self,n):

		end = {1}

		while n not in end:
			end.add(n)
			n = sum(int(d)**2 for d in str(n))

		return n == 1

s = Solution()
print(s.happyNumber(19))