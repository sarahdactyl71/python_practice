def longestCommonPrefix(self, strs):
        index = 0
        longest_prefix = ''
        while all(word[index] == strs[0][index] for word in strs) == True:
            longest_prefix += strs[0][index]
            index += 1
        return longest_prefix