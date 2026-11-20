class Solution:
    def isPalindrome(self, s: str) -> bool:
        #cleaned = s.lower().replace(" ", "")
        cleaned = "".join([c.lower() for c in s if c.isalnum()])
        print(cleaned)
        l, r = 0, len(cleaned) - 1

        while l <= r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True         