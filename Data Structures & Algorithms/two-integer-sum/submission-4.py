class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for ind, num in enumerate(nums):
            diff = target - num
            if diff in myMap:
                return [myMap[diff], ind]
            myMap[num] = ind
        return []