class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        unique = set()

        l, r = 0, 0

        for r in range(len(s)):
            # breaking condition, to update L: duplicate in set:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            # not duplicate
            unique.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length