class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, first in enumerate(nums):
            # dont use same first value if duplicate
            if idx > 0 and first == nums[idx - 1]:
                continue

            # nums[l] + nums[r] need to sum up to target - first
            l, r = idx + 1, len(nums) - 1

            while l < r:
                three_sum = first + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:  # equal
                    result.append([first, nums[l], nums[r]])
                    # update just any one, upper conditions update the other
                    # example [-2, -2, 0, 0, 2, 2]
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result