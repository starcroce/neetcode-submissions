class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_cnt_s = self._convert_str_to_dict(s)
        char_cnt_t = self._convert_str_to_dict(t)
        return self._compare_dict(char_cnt_s, char_cnt_t)

    def _convert_str_to_dict(self, s):
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

    def _compare_dict(self, d1, d2):
        if len(d1) != len(d2):
            return False
        for k in d1:
            if k not in d2:
                return False
            if d1[k] != d2[k]:
                return False
        return True