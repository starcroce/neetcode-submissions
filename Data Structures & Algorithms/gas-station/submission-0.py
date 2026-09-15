class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curr = 0
        res = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                res = i + 1
        return res