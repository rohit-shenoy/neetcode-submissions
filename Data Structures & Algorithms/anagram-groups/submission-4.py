class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        anagrapMap = defaultdict(
            list
        )  # key: tuple(list of char counts), val: list of strings

        for s in strs:
            countList = [0] * 26

            for c in s:
                countList[ord(c) - ord("a")] += 1

            anagrapMap[tuple(countList)].append(s)
        
        output = []
        for k, v in anagrapMap.items():
            output.append(v)
        return output 