def letterCombinations(digits):
    letters_mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
    }

    if len(digits) == 0:
        return []

    result = letters_mapping.get(digits, [])
    if result:
        return result

    letters = letters_mapping[digits[0]]
    for letter in letters:
        for r in letterCombinations(digits[1:]):
            result.append(letter + r)

    letters_mapping[digits] = result
    return result

digits = "23"
print(letterCombinations(digits))