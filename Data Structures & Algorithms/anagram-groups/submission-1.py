import collections 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = collections.defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]

        return [anagram_map[key] for key in anagram_map]