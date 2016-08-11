#Given a string containing just the characters 
#'(', ')', '{', '}', '[' and ']', determine if 
#the input string is valid.
#The brackets must close in the correct order, 
#"()" and "()[]{}" are all valid but "(]" and "([)]" 
#are not.

class Solution(object):
    def isValid(self, s):

    	if len(s) % 2 != 0:
    		return False

    	stack = []

    	matches = [ ('(',')'), ('[',']'), ('{','}') ]

    	opening = ('({[')

    	for paren in s:

    		if paren in opening:
    			stack.append(paren) 
    			print (stack)

    		else:

    			# first element in string must be open paren
    			# if not return False
    			if len(stack) == 0:
    				return False

    			last_open = stack.pop()

    			if (last_open,paren) not in matches:
    				return False

    	# return if opeing parens didn't have closing parens
    	return len(stack) == 0



s = Solution()
print (s.isValid('[['))