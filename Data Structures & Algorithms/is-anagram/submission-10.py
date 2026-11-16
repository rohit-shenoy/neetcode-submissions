class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = [0] * 26, [0] * 26 # chars ascii is index, vals are counts

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sMap[ord(s[i]) - ord('a')] += 1
            tMap[ord(t[i]) - ord('a')] += 1
        
        return sMap == tMap