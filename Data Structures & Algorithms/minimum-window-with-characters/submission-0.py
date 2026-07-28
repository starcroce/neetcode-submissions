class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, 0
        res_len, res_str = float("inf"), ""
        while end < len(s):
            curr = s[start:end+1]
            while self._is_present(t, curr):
                # res = min(res, len(curr))
                if len(curr) < res_len:
                    res_len = len(curr)
                    res_str = curr
                start += 1
                curr = s[start:end+1]
            end += 1
        return res_str

    def _is_present(self, s1, s2):
        char_cnt_1, char_cnt_2 = {}, {}
        for c in s1:
            char_cnt_1[c] = char_cnt_1.get(c, 0) + 1
        for c in s2:
            char_cnt_2[c] = char_cnt_2.get(c, 0) + 1
        for c in char_cnt_1:
            if c not in char_cnt_2 or char_cnt_1[c] > char_cnt_2[c]:
                return False
        return True
