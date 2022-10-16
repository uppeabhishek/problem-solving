class TweetCounts:

    def __init__(self):
        self.dict = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.dict[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        chunk = 0
        if freq == 'minute':
            chunk = 60
        elif freq == 'hour':
            chunk = 3600
        else:
            chunk = 86400
        
        result = []
                
        for i in range(startTime, endTime + 1, chunk):
            result.append(0)
                
        for ele in self.dict[tweetName]:
            if ele < startTime or ele > endTime:
                continue
            
            result[(ele - startTime) // chunk] += 1
        
        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)