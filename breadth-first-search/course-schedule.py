class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for element in prerequisites:
            u = element[0]
            v = element[1]

            graph[v].append(u)

        state = [0] * numCourses

        def dfs(node):

            # currently in this DFS path
            state[node] = 1

            for neigh in graph[node]:

                # neighbour is currently in the same DFS path
                if state[neigh] == 1:
                    return False

                # neighbour has not been visited yet
                if state[neigh] == 0:

                    if not dfs(neigh):
                        return False

            # completely processed
            state[node] = 2

            return True

        for num in range(numCourses):

            if state[num] == 0:

                if not dfs(num):
                    return False

        return True