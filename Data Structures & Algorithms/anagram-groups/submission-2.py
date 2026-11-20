class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list) # key: sorted str, val = []

        for s in strs:
            arranged = sorted(s)
            anagramMap[tuple(arranged)].append(s)

        return list(anagramMap.values())

