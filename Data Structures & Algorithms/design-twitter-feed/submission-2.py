import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.follow_map = {}
        self.tweet_map = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_tweets = self.tweet_map.get(userId, [])
        user_tweets.append((-self.timestamp, tweetId))
        if len(user_tweets) > 10:
            user_tweets.pop(0)
        self.tweet_map[userId] = user_tweets
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follow_set = set(self.follow_map.get(userId, set()))
        follow_set.add(userId)
        heap = []
        for uid in follow_set:
            for ts, tid in self.tweet_map.get(uid, []):
                heapq.heappush(heap, (ts, tid))
        return [tid for _, tid in heapq.nsmallest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        follow_set = self.follow_map.get(followerId, set())
        follow_set.add(followeeId)
        self.follow_map[followerId] = follow_set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follow_set = self.follow_map.get(followerId, set())
        if followeeId in follow_set:
            follow_set.remove(followeeId)
            self.follow_map[followerId] = follow_set