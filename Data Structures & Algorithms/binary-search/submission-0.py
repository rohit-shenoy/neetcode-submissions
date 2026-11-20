class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # for nums = [1], they can be same is the logic
        while l <= r:
            mid = l + (
                (r - l) // 2
            )  # python integers unbounded, no overflow but still best practice

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        # not found if pointers cross over
        return -1