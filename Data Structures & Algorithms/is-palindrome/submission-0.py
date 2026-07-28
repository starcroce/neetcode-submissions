class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if "0" <= c <= "9" or "a" <= c <= "z" or "A" <= c <= "Z":
                new_s.append(c.lower())
        start, end = 0, len(new_s) - 1
        while start <= end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True