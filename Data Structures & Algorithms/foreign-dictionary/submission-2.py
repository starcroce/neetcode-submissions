from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {}
        for w in words:
            for c in w:
                adj_list[c] = set()
        indegrees = {c: 0 for c in adj_list}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                        indegrees[c2] += 1
                    break

        queue = deque([c for c in indegrees if indegrees[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for nei in adj_list[c]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        if len(res) != len(indegrees):
            return ""
        return "".join(res)