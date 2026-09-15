from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)
        num_cnt = Counter(hand)
        for n in hand:
            if num_cnt[n] > 0:
                for i in range(n, n + groupSize):
                    if num_cnt[i] == 0:
                        return False
                    num_cnt[i] -= 1
        return True