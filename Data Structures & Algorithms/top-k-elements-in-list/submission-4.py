class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequencies list which stores at index = counts, a list of the nums
        # works because size is bounded by length of nums, at max all nums equal, max
        # frequency = len(nums)

        countMap = defaultdict(int)
        
        for num in nums:
            countMap[num] += 1

        frequencies = [[] for _ in range(len(nums) + 1)]

        for num, count in countMap.items():
            frequencies[count].append(num)
        
        output = []
        # k is atleast one
        for ind in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[ind]:
                output.append(num)

                if len(output) == k:
                    return output