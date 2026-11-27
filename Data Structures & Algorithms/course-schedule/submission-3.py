class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i:[] for i in range(numCourses)} # adj list: crs:[pre]
        visiting = set()

        # construct pre-req map
        for course, pre in prerequisites:
            preReqMap[course].append(pre)
        

        def canComplete(course):
            if course in visiting:
                return False
            
            if preReqMap[course] == []:
                return True
            
            # attempt completing
            visiting.add(course)

            for pre in preReqMap[course]:
                if not canComplete(pre):
                    return False
            
            visiting.remove(course)
            preReqMap[course] = []
            return True

        for i in range(numCourses):
            if not canComplete(i):
                return False
        return True
