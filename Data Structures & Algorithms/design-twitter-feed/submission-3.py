import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.follow_map[userId])
        users.add(userId)
        heap = []
        for uid in users:
            tweets = self.tweet_map[uid]
            if tweets:
                idx = len(tweets) - 1
                ts, tid = tweets[idx]
                heapq.heappush(heap, (-ts, tid, uid, idx))
        res = []
        while heap and len(res) < 10:
            _, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx - 1 >= 0:
                next_ts, next_tid = self.tweet_map[uid][idx - 1]
                heapq.heappush(heap, (-next_ts, next_tid, uid, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
