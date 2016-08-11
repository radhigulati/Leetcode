class Solution(object):
	def happyNumber(self,n):

		end = {1}

		while n not in end:
			end.add(n)
			print(end)
			n = sum(int(d)**2 for d in str(n))

		return n == 1

s = Solution()
print(s.happyNumber(15))