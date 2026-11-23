

class Solution:
    def simplifyPath(self, path: str) -> str:
    ### Split on /. "/a/./b/../../c/".split("/") gives ['', 'a', '.', 'b', '..', '..', 'c', '']. Duplicate and leading or trailing slashes become empty strings, which you simply skip. Process each part using the rules table: A folder name: push it onto the stack. ..: pop from the stack, if it's not empty.. or empty: do nothing. Rebuild the path: "/" + "/".join(stack)
###
        
        stack = []

        for part in path.split("/"):
            if part == "..":
                if stack:          # can't go above root
                    stack.pop()
            elif part and part != ".":
                stack.append(part)  # a real folder name
            # else: "" or "." -> ignore

        return "/" + "/".join(stack)