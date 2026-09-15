class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = set()
        tt1, tt2, tt3 = target
        for t1, t2, t3 in triplets:
            if t1 > tt1 or t2 > tt2 or t3 > tt3:
                continue
            if t1 == tt1:
                merged.add(1)
            if t2 == tt2:
                merged.add(2)
            if t3 == tt3:
                merged.add(3)
        return len(merged) == 3