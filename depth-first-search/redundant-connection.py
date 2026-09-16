class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        graph = [[] for _ in range(n + 1)]

        def dfs(node, dest, visited):

            if node == dest:
                return True

            visited[node] = True

            for neigh in graph[node]:

                if not visited[neigh]:

                    if dfs(neigh, dest, visited):
                        return True

            return False

        for edge in edges:

            u = edge[0]
            v = edge[1]

            visited = [False] * (n + 1)

            # Pehle check karo:
            # kya u se v tak already path exist karta hai?
            if dfs(u, v, visited):
                return edge

            # Agar path nahi hai, toh edge add kar do
            graph[u].append(v)
            graph[v].append(u)

        return []