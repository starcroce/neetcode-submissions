from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            indegrees[dst] += 1
            adj_list[src].append(dst)

        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for n in adj_list[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)

        if len(res) == numCourses:
            return res
        return []