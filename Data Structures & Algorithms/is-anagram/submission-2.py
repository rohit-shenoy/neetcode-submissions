import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keys_s, keys_t = collections.defaultdict(int), collections.defaultdict(int)
        
        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            keys_s[s[idx]] += 1
            keys_t[t[idx]] += 1

        return keys_s == keys_t