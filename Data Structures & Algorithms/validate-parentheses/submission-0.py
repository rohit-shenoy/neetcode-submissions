class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {"}": "{", ")": "(", "]": "["}

        for c in s:
            # closing
            if c in close_to_open:
                # there should be something to pop, and it should match
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            # opening
            else:
                stack.append(c)

        return True if not stack else False
