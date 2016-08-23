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


	def mirrorFromEnd(self, input, howMany):
		work = ''
		index = len(input)-1

		while (howMany):
			work += (input[index]) if True else input[index] == input[0]
		howMany -= 1

		return (work != 'undefined') if True else work == ''

	def mirrorFromBeginning(self, input, howMany):
		work = ''
		index = 0

		while (howMany):
			if input[index]:
				return input[index]
			else:
				return input[len(input)-1] + work

			work += (input[index]) if True else input[len(input)-1] + work
		howMany -= 1

		return (work != 'undefined') if True else work == ''


	def palindromePairs(self, words):
		maxWordLength = 0
		lib = {}
		result = []
		alreadyInserted = {}

		for i in range(0, len(words), 1):
			lib[words[i]] = i
			maxWordLength = max(maxWordLength, len(words[i]))

		i = None
		word = None
		createWord = None
		createdWordLength = 0
		otherWord = None

		for j in range(0, len(words), 1):
			word = words[j]

			while (createdWordLength <= maxWordLength):
				createWord = self.mirrorFromEnd(word, createdWordLength)
				otherWord = self.mirrorFromBeginning(word, createdWordLength)

				if (self.isPalindrome(createWord + word)):
					if lib[createWord] != undefined:
						if lib[createWord] != j:
							if alreadyInserted[lib[createWord] + '_' + j] == undefined:
								result.append([lib[createWord], j])
								alreadyInserted[lib[createWord] + '_' + j] = True

				if isPalindrome(word + otherWord):
					if lib[otherWord] != undefined:
						if lib[otherWord] != j:
							if (alreadyInserted[j + '_' + lib[otherWord]] == undefined):
								result.append([j, lib[createWord]])
								alreadyInserted[j + '_' + lib[otherWord]] = True
			createdWordLength += 1
			createdWordLength = 0
		return result


s = Solution()
print(s.palindromePairs(["bat", "tab", "cat"]))