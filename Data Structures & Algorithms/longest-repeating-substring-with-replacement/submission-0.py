class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cnt = {}
        start = 0
        max_freq = 0
        res = 0

        for end in range(len(s)):
            char_cnt[s[end]] = char_cnt.get(s[end], 0) + 1
            max_freq = max(max_freq, char_cnt[s[end]])

            while end - start + 1 > max_freq + k:
                char_cnt[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)
        
        return res