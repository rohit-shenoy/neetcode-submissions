class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for num, start, end in trips:
            diff[start] += num   # pick up
            diff[end] -= num     # drop off (passengers are out at `end`)

        load = 0
        for change in diff:
            load += change
            if load > capacity:
                return False
        return True