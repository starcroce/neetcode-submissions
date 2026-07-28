from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_map = defaultdict(list)
        for ui, vi, ti in times:
            node_map[ui].append((vi, ti))
        node_time = {i: float("inf") for i in range(1, n+1)}
        
        queue = deque([(k, 0)])
        node_time[k] = 0

        while len(queue):
            node, curr = queue.popleft()
            if node_time[node] < curr:
                continue
            for nei, t in node_map[node]:
                if curr + t < node_time[nei]:
                    node_time[nei] = curr + t
                    queue.append((nei, curr + t))
            
        res = max(node_time.values())
        if res == float("inf"):
            return -1
        else:
            return res