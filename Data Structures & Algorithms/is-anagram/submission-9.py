class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = defaultdict(int), defaultdict(int) # key: char, val = counts

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        
        return sMap == tMap