class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = defaultdict(int) # char: count for window l - r
        longest = 0
        l = 0


        # {X: 1, Y: 2}
        for r in range(len(s)):
            charCounts[s[r]] += 1
            
            #breaking condition = no. of replaceable chars > k -> shrink window 
            while ((r - l + 1) - max(charCounts.values()) > k):
                charCounts[s[l]] -= 1
                l += 1

            # valid window
            longest = max(longest, r - l + 1)

        return longest
        