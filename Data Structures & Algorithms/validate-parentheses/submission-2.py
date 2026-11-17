class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {'(':')', '{':'}', '[':']'}
        stack = [] #append and pop from right

        # Iterate through the string, if open push to stack
        # If close, pop from stack, and check for match / mismatch
        # If mismatch return, match continue
        # Return true if stack is empty (no open openers)

        for char in s:
            # open 
            if char in openToClose.keys():
                stack.append(char)
            # closing
            else:
                if not stack:
                    return False
                # non-empty
                popped = stack.pop()
                if not char == openToClose[popped]:
                    return False
        return len(stack) == 0

                