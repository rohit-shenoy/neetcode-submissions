class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left, right, final = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        # [1, 2, 4, 6]
        l_prod, r_prod = 1, 1
        
        for idx in range(len(nums)):
            left[idx] = l_prod
            l_prod *= nums[idx]

        for rev in range(len(nums) - 1, -1, -1):
            right[rev] = r_prod
            r_prod *= nums[rev]
        
        print(left)
        print(right)
        
        for i in range(len(left)):
            final[i] = left[i] * right[i]
        
        return final