class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prereq list, example, course 1 has two pre-req 3 and 4 is rep. as {1: [3, 4]}
        pre_map = {i: [] for i in range(num_courses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # used to maintain or detect duplicates (cycles) along the current visit or DFS traversal
        visit = set()

        def dfs(crs: int) -> bool:
            ### Helper to check if each crs can be completed or not

            if crs in visit:
                # cycle while visiting
                return False

            # no pre-req, can complete
            if pre_map[crs] == []:
                return True

            # start visiting, dfs on pre-req, and once finished, mark as can complete, and unvisit
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            # can complete so mark
            pre_map[crs] = []
            visit.remove(crs)
            return True

        # visit all courses
        for i in range(num_courses):
            if not dfs(i):
                return False
        return True