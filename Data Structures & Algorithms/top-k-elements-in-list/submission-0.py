class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = defaultdict(int)
        for n in nums:
            num_cnt[n] += 1
        num_cnt_pairs = [(n, num_cnt[n]) for n in num_cnt]
        sorted_num_cnt = sorted(num_cnt_pairs, key=lambda x: x[1], reverse=True)
        res = [x[0] for x in sorted_num_cnt][:k]
        return res