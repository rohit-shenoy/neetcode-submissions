class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        chars = defaultdict(int)

        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1

            # can no longer expand - make sure window is valid
            while (r - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1

            # can add chars still
            result = max(
                result,
                r - l + 1,
            )

        return result