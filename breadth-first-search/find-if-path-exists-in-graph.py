class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n) ]
        for edge in edges:
            v = edge[1]
            u = edge[0]
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        queue = []
        front = 0
        queue.append(source)
        visited[source] = True
        while front<len(queue):
            node = queue[front]
            front+=1
            if node==destination:
                return True
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)
        return False