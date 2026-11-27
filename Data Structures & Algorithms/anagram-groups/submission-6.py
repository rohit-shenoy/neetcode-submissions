class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        result = []
        anagramMap = defaultdict(list) # key: tuple(charCountList), value: word

        for word in strs:
            charCountList = [0] * 26 # index = ASCII of char, store count

            for c in word:
                charCountList[ord(c) - ord('a')] += 1
            
            anagramMap[tuple(charCountList)].append(word)
        
        for _, v in anagramMap.items():
            result.append(v)
        return result