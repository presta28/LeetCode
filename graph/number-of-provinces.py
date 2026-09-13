class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n+1)]  
        count=0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = [False]*(n+1)
        for k in range(n):
            if visited[k]:
                continue
            count+=1
            queue = []
            front = 0
            queue.append(k)
            visited[k] = True
            while front<len(queue):
                node = queue[front]
                front+=1
                for neigh in graph[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        queue.append(neigh)
            
        return count