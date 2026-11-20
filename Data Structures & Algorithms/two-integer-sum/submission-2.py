class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N) time and O(N) space
        myMap = {} # key: num, val: ind

        for i, num in enumerate(nums):
            diff = target - num
            if diff in myMap:
                return [myMap[diff], i]
            myMap[num] = i
        return [-1, -1]