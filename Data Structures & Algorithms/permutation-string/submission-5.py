import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        chars_s1, chars_s2 = collections.defaultdict(int), collections.defaultdict(int)

        for idx, c1 in enumerate(s1):
            chars_s1[c1] += 1
            chars_s2[s2[idx]] += 1

        l, r = 0, len(s1) - 1

        while r < len(s2):
            if chars_s1 == chars_s2:
                return True
            else:
                # slide
                if chars_s2[s2[l]] == 1:
                    del chars_s2[s2[l]]
                else:
                    chars_s2[s2[l]] -= 1
                l += 1

                r += 1
                if r < len(s2):
                    chars_s2[s2[r]] += 1
        return False

