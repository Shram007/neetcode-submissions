class Twitter:

    def __init__(self):
        self.time = 0 # increases when someone posts a tweet
        self.followMap = defaultdict(set) # set of users they follow
        self.tweetMap = defaultdict(list) # list of (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])
        
        feed.sort(key= lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
