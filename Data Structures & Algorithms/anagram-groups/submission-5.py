class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        anagramMap = defaultdict(list) # hashmap of key: []

        for s in strs:
            chars = [0] * 26 # counts of chars, index = ASCII (char)

            for c in s:
                chars[ord(c) - ord('a')] += 1
            
            anagramMap[tuple(chars)].append(s)
        
        output = []
        for _, v in anagramMap.items():
            output.append(v)
        return output
            