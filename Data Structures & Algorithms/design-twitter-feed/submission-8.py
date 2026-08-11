class Twitter:

    def __init__(self):
        # set of userIds they follow
        self.following = defaultdict(set)
        # list of (counter, tweetId) for each user
        self.tweets = defaultdict(list)
        # global tweet ordering
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # loop through all the followers and itself
        # add the tweets to a list in order of recency checking the tweet[userId] = (counter, tweetId)
        # use a min heap and sice it gives you the smallest item store the counters as negatives
        result = []
        min_heap = []

        users = self.following[userId]
        users.add(userId)

        for user in users:
            tweetList = self.tweets[user]

            if tweetList:
                index = len(tweetList) - 1
                time, tweetId = tweetList[index]
            
                heapq.heappush(min_heap, (-time, tweetId, user, index))
        
        while min_heap and len(result) < 10:
            time, tweetId, user, index = heapq.heappop(min_heap)

            result.append(tweetId)

            if index - 1 >= 0:
                nextTime, nextTweetId = self.tweets[user][index - 1]

                heapq.heappush(min_heap, (-nextTime, nextTweetId, user, index - 1))

        return result

        # for follow in self.following[userId]:
        #     tweetsList = self.tweets[follow]
        #     for tweet in tweetsList:
        #         heapq.heappush(min_heap, (-tweet[0], tweet[1]))
        
        # for tweet in self.tweets[userId]:
        #     heapq.heappush(min_heap, (-tweet[0], tweet[1]))
        
        # for _ in range(10):
        #     if not min_heap:
        #         break
        #     tweet = heapq.heappop(min_heap)
        #     result.append(tweet[1])
        
        # return result

    # user followerId follows user followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        # keep a hashmap that has the user and who they follow
        # key = user
        # value = users following
        # add to the hashmap location when they follow someone
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove from users following (the hashmap) when they unfollow someone
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
