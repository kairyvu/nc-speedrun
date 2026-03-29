class Twitter:

    def __init__(self):
        self.userToFollowing = defaultdict(set)
        self.userToPost = defaultdict(deque)
        self.tweetIndex = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToPost[userId].append((self.tweetIndex, tweetId))
        self.tweetIndex += 1
        if len(self.userToPost[userId]) > 10:
            self.userToPost[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        self.userToFollowing[userId].add(userId)
        minHeap = []
        for followee in self.userToFollowing[userId]:
            for post in self.userToPost[followee]:
                heapq.heappush(minHeap, post)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            _, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        return list(reversed(res))


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].discard(followeeId)
