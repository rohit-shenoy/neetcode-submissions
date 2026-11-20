class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strings = []
        idx = 0

        while idx < len(s):
            j = idx
            while s[j] != "#":
                j += 1

            word_len = int(s[idx:j])
            strings.append(s[j + 1 : j + 1 + word_len])
            idx = j + 1 + word_len

        return strings