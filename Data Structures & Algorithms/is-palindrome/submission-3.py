class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Contraints & validation:
        # s.length > 1 so non-empty

        # inline helper
        def isAlphaNumeric(c: str) -> bool:
            if (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9')
            ):
                return True
            return False

        # Use two pointers at start, end of string
        # If its not alphanumeric, skip
        # If it is, compare lowercase, move pointers inwards

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlphaNumeric(s[l]):
                l += 1
            while l < r and not isAlphaNumeric(s[r]):
                r -= 1
            # chars are alphanumeric here
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True