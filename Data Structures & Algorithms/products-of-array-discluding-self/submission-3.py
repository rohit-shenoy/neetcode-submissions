class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Clarifying questions / assumptions - atleast 2, negatives, 0

        left, right, output = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        # [1, 2, 4, 6]
        prodL = 1
        for i in range(len(nums)):
            left[i] = left[i] * prodL
            prodL = prodL * nums[i]
        
        prodR = 1
        for j in range(len(nums) - 1, -1, -1):
            right[j] = right[j] * prodR
            prodR *= nums[j]
        
        for k in range(len(output)):
            output[k] = left[k] * right[k]
        return output