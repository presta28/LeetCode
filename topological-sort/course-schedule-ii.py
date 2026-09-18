class Solution:
    def findOrder(self, numCourses: int, preq: list[list[int]]) -> list[int]:
        queue = []
        answer = []
        indegree = [0]*numCourses
        outdegree = [[] for _ in range(numCourses)]
        for elemnt in preq:
            u = elemnt[0]
            v = elemnt[1]
            outdegree[v].append(u)
            indegree[u]+=1
        def fun():
            nonlocal queue
            nonlocal indegree
            nonlocal answer
            nonlocal outdegree
            while len(queue)!=0:
                node = queue.pop(0)
                answer.append(node)
                for neigh in outdegree[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        queue.append(neigh)
            return answer
        for num in indegree:        
            if num ==0:
                queue.append(num)
                result = fun()
                break
        if len(answer)!=numCourses:
            return []
        else:
            return answer