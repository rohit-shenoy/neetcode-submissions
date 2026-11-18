class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int) # key: char, val: count

        l = 0
        longest = 0

        for r in range(len(s)):
            charMap[s[r]] += 1
            
            # condition not satisfied - slide l, remove from window until satisfied
            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1 
            # valid window
            longest = max(longest, r - l + 1)
        return longest

