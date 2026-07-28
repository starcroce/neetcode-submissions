class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

        for c in s:
            if c in char_map:
                stack.append(c)
            else:
                if len(stack) == 0 or char_map[stack[-1]] != c:
                    return False
                stack.pop()

        return len(stack) == 0
