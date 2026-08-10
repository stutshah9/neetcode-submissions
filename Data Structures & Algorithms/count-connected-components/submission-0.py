class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # save the edges in a dictionary
        # cannot set the default value to an int (should be none because some nodes might not have connections)
        edgesDict = defaultdict(list)

        visited = set()

        components = 0

        for edge in edges:
            edgesDict[edge[0]].append(edge[1])
            edgesDict[edge[1]].append(edge[0])
        # key = vertex
        # value = edge
        # use a for loop to run through the values of the keys of the dictionary
        for i in range(n):
        # if the node is not in the visited set
            if i not in visited:
        # increment the components counter
                components += 1
        # run a DFS algorithm starting form the first vertex using the dictionary
                self.DFS(i, edgesDict, visited)
        # if the node is in the visited set, skip it
        
        return components

    def DFS(self, vertex, edgesDict, visited):
        visited.add(vertex)
        for neighbor in edgesDict[vertex]:
            if neighbor not in visited:
                self.DFS(neighbor, edgesDict, visited)