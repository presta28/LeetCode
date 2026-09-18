class Solution:
    def findOrder(self, numCourses: int, preq: list[list[int]]) -> list[int]:
        queue = []
        answer = []
        front=0
        indegree = [0]*numCourses
        outdegree = [[] for _ in range(numCourses)]
        for elemnt in preq:
            u = elemnt[0]
            v = elemnt[1]
            outdegree[v].append(u)
            indegree[u]+=1
        for i in range(numCourses):      
            if  indegree[i]==0:
                queue.append(i)
        while front<len(queue):
            node = queue[front]
            front+=1
            answer.append(node)
            for neigh in outdegree[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        if len(answer) != numCourses:
            return []

        return answer
        