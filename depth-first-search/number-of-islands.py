class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:         
        count=0
        visited = set()
        graph = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                graph[(i, j)] = []

                if i - 1 >= 0:
                    graph[(i, j)].append((i - 1, j))

                if i + 1 < len(grid):
                    graph[(i, j)].append((i + 1, j))

                if j - 1 >= 0:
                    graph[(i, j)].append((i, j - 1))

                if j + 1 < len(grid[0]):
                    graph[(i, j)].append((i, j + 1))
        def dfs(node:tuple):
            if grid[node[0]][node[1]] == "0":
                return
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        for key in graph:
            if key in visited:
                continue
            if grid[key[0]][key[1]] == "1":
                dfs(key)
                count+=1
        return count