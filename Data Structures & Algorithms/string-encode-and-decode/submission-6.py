class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + '*' + s
        return encoded

    # 5#Hello5#World4#Neet4#Code
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '*':
                j += 1
            # when this breaks, i to j is the wordLength
            wordLength = int(s[i:j])
            word = s[j + 1: j + 1 + wordLength]
            decoded.append(word)
            i = j + 1 + wordLength
        return decoded