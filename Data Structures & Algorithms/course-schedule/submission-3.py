class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the courses are nodes in the graph
        # the prerequisites are edges
        # loop through each of the courses
        # perform DFS on them through their prerequisites
        # have a set that tracks the path
        # if the course is already in the set that course cannot be taken
        # keep track of the number of courses that can be taken
        # if its less than the number of courses return false

        safeCourses = set()

        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            graph[course].append(prereq)

        for i in range(numCourses):
            startNode = i

            setPath = set()
            setPath.add(startNode)

            noCycle = self.DFS(graph, startNode, setPath, safeCourses)

            if not noCycle:
                return False
            
        return True

    def DFS(self, graph, course, setPath, safeCourses) -> bool:

        if course in safeCourses:
            return True

        for pre in graph[course]:

            if pre in setPath:
                return False

            setPath.add(pre)

            result = self.DFS(graph, pre, setPath, safeCourses)
            if result == False:
                return False
            
            setPath.remove(pre)
        
        safeCourses.add(course)

        return True
