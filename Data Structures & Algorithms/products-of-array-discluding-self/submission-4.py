class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        prodL, prodR = 1, 1

        #   [1, 2, 4, 6]
        # L [1, 1, 2, 8]
        # R [48, 24, 6, 1]
        # Traverse ->, <-, for each element, calculate prod of all elements l / r
        for i in range(len(nums)):
            left[i] = prodL
            prodL = prodL * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right[i] = prodR
            prodR = prodR * nums[i]
        
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        
        return result