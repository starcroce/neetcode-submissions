class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        for i in range(len(s2)-len(s1)+1):
            substr = s2[i:i+len(s1)]
            if self._is_permutation(s1, substr):
                return True
        return False
    
    def _is_permutation(self, s1, s2):
        print(s1, s2)
        char_cnt_1, char_cnt_2 = {}, {}
        for c in s1:
            char_cnt_1[c] = char_cnt_1.get(c, 0) + 1
        for c in s2:
            char_cnt_2[c] = char_cnt_2.get(c, 0) + 1
        for c in char_cnt_1:
            if c not in char_cnt_2 or char_cnt_1[c] != char_cnt_2[c]:
                return False
        return True