class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dictionary that keeps track of the courses and their prerequisites
        dict = defaultdict(list)
        for crs, pre in prerequisites:
            dict[crs].append(pre)
        
        # store all the courses along the first DFS path
        visitSet = set()

        def dfs(crs):
            # if course has already been visited there is a cycle
            if crs in visitSet:
                return False
            
            # if the course has no prerequisites the course can definitly be completed 
            if dict[crs] == []:
                return True
            
            visitSet.add(crs)
            for prer in dict[crs]:
                if not dfs(prer):
                    return False
            visitSet.remove(crs)
            dict[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
