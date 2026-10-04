class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Hashmap of counts, key: num, val: counts
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # construct freq list (bounded by size of nums)
        frequencies = [[] for x in range(len(nums) + 1)]

        for num, count in counts.items():
            frequencies[count].append(num)

        # get top k
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return        