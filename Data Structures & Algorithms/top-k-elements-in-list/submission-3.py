class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create dict with counts
        countDict = defaultdict(int)
        for num in nums:
            countDict[num] += 1
        
        # at index i, store [] with elements having count i
        frequencies = [[] for i in range(len(nums) + 1)] 
        
        for num, count in countDict.items():
            frequencies[count].append(num)

        output = []
        # Iterate in reverse order
        for x in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[x]:
                output.append(num)
                if len(output) == k:
                    return output
        