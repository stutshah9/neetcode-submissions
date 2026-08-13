class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # have a results array
        result = []
        completed = set()
        # create a hashmap with the class and it's prerequisites
        courses = defaultdict(list)
        # key = course
        # value = list of prerequisites
        for course, pre in prerequisites:
            courses[course].append(pre)

        for i in range(numCourses):
            if i in completed:
                continue 
        # have a visited set to keep track of the courses already visited in that BFS track
            visited = set()
            if self.isCycle(i, visited, completed, courses, result):
                return []

        return result

    def isCycle(self, i, visited, completed, courses, result) -> bool:
        visited.add(i)
        # loop through the prerequisites of the course
        for pre in courses[i]:
            if pre in visited:
                return True
            
            if pre in completed:
                continue

        # find if those prerequisites have any prerequisites through recursion
            if self.isCycle(pre, visited, completed, courses, result):
                return True
        
        visited.remove(i)

        completed.add(i)
        result.append(i)
        return False
