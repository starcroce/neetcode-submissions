from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for next_c in adj_list[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)

        if len(res) == numCourses:
            return res
        return[]