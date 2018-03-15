class Twitter:
    def __init__(self):
        from collections import defaultdict
        self.follow_list = defaultdict(list)
        self.followed_by_list = defaultdict(list)
        self.tweet_list = defaultdict(list)

    def postTweet(self, userId, tweetId):
        from time import time
        tweet = (tweetId, time(), userId)
        self.tweet_list[userId].append(tweet)
        for user in self.followed_by_list[userId]:
            self.tweet_list[user].append(tweet)

    def getNewsFeed(self, userId):
        return list(map(lambda x: x[0], sorted(self.tweet_list[userId], key=lambda x: x[1], reverse=True)[:10]))

    def follow(self, followerId, followeeId):
        if not followerId == followeeId and not followerId in self.followed_by_list[followeeId] \
                and not followeeId in self.follow_list[followerId]:
            self.followed_by_list[followeeId].append(followerId)
            self.follow_list[followerId].append(followeeId)
            for tweet in [tweet for tweet in self.tweet_list[followeeId] if tweet[2] == followeeId][-10:]:
                self.tweet_list[followerId].append(tweet)

    def unfollow(self, followerId, followeeId):
        if not followerId == followeeId:
            if followerId in self.followed_by_list[followeeId]:
                self.followed_by_list[followeeId].remove(followerId)
            if followeeId in self.follow_list[followerId]:
                self.follow_list[followerId].remove(followeeId)
            for tweet in self.tweet_list[followeeId]:
                if tweet in self.tweet_list[followerId] and tweet[2] == followeeId:
                    self.tweet_list[followerId].remove(tweet)


if __name__ == '__main__':
    twitter = Twitter()
    func = ["postTweet", "follow", "follow", "getNewsFeed", "postTweet", "getNewsFeed", "getNewsFeed", "unfollow",
            "getNewsFeed", "getNewsFeed", "unfollow", "getNewsFeed", "getNewsFeed"]
    args = [[1, 5], [1, 2], [2, 1], [2], [2, 6], [1], [2], [2, 1], [1], [2], [1, 2], [1], [2]]
    for i in range(len(func)):
        res = getattr(twitter, func[i])(*args[i])
        if func[i] == 'getNewsFeed':
            print(res)
