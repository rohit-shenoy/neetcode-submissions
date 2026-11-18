class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            # if its in charSet, move window until its not
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # new char
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
        return maxLength
