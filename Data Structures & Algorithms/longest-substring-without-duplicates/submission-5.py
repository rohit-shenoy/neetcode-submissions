class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        if not s:
            return longest
        
        l = 0
        chars = set() # stores chars in the window l-r
        
        for r in range(len(s)):
            # breaking condition - remove until no duplicates
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            longest = max(longest, r - l + 1)

        return longest            

