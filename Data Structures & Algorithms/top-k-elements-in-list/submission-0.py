class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = collections.defaultdict(int)

        for idx in range(len(nums)):
            counts_map[nums[idx]] += 1

        # create BOUNDED array
        bounded = [[] for i in range(len(nums) + 1)]

        # at index count, append number to the list
        for number, counts in counts_map.items():
            bounded[counts].append(number)

        result = []
        for i in range(len(bounded) - 1, 0, -1):
            for number in bounded[i]:
                result.append(number)
                if len(result) == k:
                    return result