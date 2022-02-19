#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings = []
        for i in range(n):
            meetings.append((start[i], end[i]))
        meetings.sort(key=lambda k: k[1])

        last_val = -1

        res = 0

        for meeting in meetings:
            if meeting[0] > last_val:
                last_val = meeting[1]
                res += 1

        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends