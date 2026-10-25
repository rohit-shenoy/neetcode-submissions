class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Validation: atleast two numbers, target etc, always one soln

        # Approach: array is sorted (non-dec), so can use two pointers, left, right, check sum, if greater than target then dec r, else inc l.
        # 1, 2, 4, 4, 5, 7      Target: 7
        l, r = 0, len(numbers) - 1
        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l+1, r+1]
            elif currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
        return [-1, -1]
