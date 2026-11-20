class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_map = {}  # num: index

        for idx, current_num in enumerate(nums):
            if target - current_num in seen_map:
                return [seen_map[target - current_num], idx]
            seen_map[current_num] = idx

        # default
        return []