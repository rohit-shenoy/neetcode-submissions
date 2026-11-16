class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} # key: num, val: index

        for ind, num in enumerate(nums):
            if (target - num) in prevMap:
                return [prevMap[target - num], ind]
            prevMap[num] = ind
        return 
            