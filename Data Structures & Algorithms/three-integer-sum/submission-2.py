class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for ind, num in enumerate(nums):
            if ind > 0 and nums[ind - 1] == nums[ind]:
                continue

            l, r = ind + 1, len(nums) - 1

            while l < r:
                currSum = num + nums[l] + nums[r]

                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                elif currSum == 0:
                    # found
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    l += 1
        return res
