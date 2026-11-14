class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotationIndex = -1

        l, r = 0, len(nums) - 1
        while l <= r:
            # if at any point, whole thing is sorted
            if nums[l] < nums[r]:
                rotationIndex = l
                break

            mid = (l + r) // 2
            rotationIndex = mid
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        # when this breaks, we have two sorted lists 0 - rotation index and rot. index 
        index1 = self.binarySearch(nums[0: rotationIndex + 1], target)
        index2 = self.binarySearch(nums[rotationIndex: ], target)

        if index1 != -1: return index1
        elif index2 != -1: return rotationIndex + index2
        else:
            return -1

    def binarySearch(self, nums:List[int], target: int) -> int:
        # Helper - list here is always sorted

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l)//2)

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
        return -1