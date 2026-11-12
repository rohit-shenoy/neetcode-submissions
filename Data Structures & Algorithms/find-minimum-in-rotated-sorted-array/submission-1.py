class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Two pointers l, r at ends
        # 2. Check if flip happens between l, r
        # 3. Get num[mid] and check if flip happens between l,m
        # 4. If yes, cut out the right half, min is in between l,m
        # 5. If not, cut out left half, min is between m, r
        # 6. Keep doing this until we converge on min number

        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            # if at any point l to r is sorted, then compare current min to nums[l] and end
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            mid = (l + r) // 2
            # check if left to mid is sorted (then search right)
            # or right to mid is sorted (then search left)
            minimum = min(minimum, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minimum