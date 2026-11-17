class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        # -1,0,1,2,-1,-4
        # [-4, -1, -1, 0, 1, 2]

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # new number + twosum
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = num + nums[l] + nums[r]
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                # match
                elif currentSum == 0:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    # handle duplicates, slide l until new number
                    while l < r and nums[l] == nums[l - 1]:
                        l+= 1
        return output