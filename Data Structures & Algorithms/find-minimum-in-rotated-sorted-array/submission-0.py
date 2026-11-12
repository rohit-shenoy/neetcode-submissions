class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Two pointers l, r at ends
        # 2. Check if flip happens between l, r
        # 3. Get num[mid] and check if flip happens between l,m
        # 4. If yes, cut out the right half, min is in between l,m
        # 5. If not, cut out left half, min is between m, r
        # 6. Keep doing this until we converge on min number

        l, r = 0, len(nums) - 1
        res = nums[0]
        #[1 2 3 4 5] -> [3 4 5 1 2] [5 1 2 3 4]
        while l <= r:
            # whole sorted part found
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res