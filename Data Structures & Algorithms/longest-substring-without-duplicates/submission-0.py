class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        visited = set()
        res = 0
        while start < len(s) and end < len(s):
            if s[end] not in visited:
                visited.add(s[end])
                res = max(res, end - start + 1)
                end += 1
            else:
                visited.remove(s[start])
                start += 1
        return res