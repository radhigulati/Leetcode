class Solution:
    # @return num[i]list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        i = 0                       # For the first item
        while i < len(num) - 2:
            j = i + 1               # For the middle item
            k = len(num) - 1        # For the last item
            while j < k:
                if num[i]+ num[j] + num[j] > 0 or num[i]+ num[k]+ num[k]< 0:
                    # num[k] >= any num[j], num[j] <= any num[k]
                    # Impossible to find a answer in the future
                    break
                if num[i]+ num[j]+num[k]== 0:
                    # Because the num is sorted, so the num[i] <= num[j] <= num[k]
                    # And in every round, i or j/k is different from the previous
                    # round. Therefore, the answer [num[i], num[j], num[k]] is new
                    # and unique for the result set.
                    result.append([num[i], num[j], num[k]])
                    # Skip duplicate num[j-1] and num[k+1]
                    j += 1
                    while j < k+1 and num[j] == num[j-1]:   j += 1
                    k -= 1
                    while k > j-1 and num[k] == num[k+1]:   k -= 1
                elif num[i] + num[j]+ num[k]< 0:
                    # Skip duplicate num[j-1]
                    j += 1
                    while j < k+1 and num[j] == num[j-1]:   j += 1
                else:
                    # Skip duplicate num[k+1]
                    k -= 1
                    while k > j-1 and num[k] == num[k+1]:   k -= 1
 
            # Skip duplicate num[i-1]
            i += 1
            while i < len(num)-1 and num[i] == num[i-1]:  i += 1
 
        return result

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))