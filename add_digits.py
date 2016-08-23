class Solution(object):
    def addDigits(self, num):

    	end = set()

    	while num not in end:
    		end.add(num)
    		num = sum(int(d) for d in str(num))

    	return num

s = Solution()
print(s.addDigits(38))