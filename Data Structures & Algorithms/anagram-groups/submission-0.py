from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_to_str = defaultdict(list)
        for s in strs:
            base = "".join(sorted(s))
            base_to_str[base].append(s)
        res = []
        for b in base_to_str:
            res.append(base_to_str[b])
        return res
