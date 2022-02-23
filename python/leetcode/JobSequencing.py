class Solution:

    def JobScheduling(self, Jobs, n):
        jobs = [False] * 100
        Jobs.sort(key=lambda k: -k.profit)
        profit, cnt = 0, 0
        for job in Jobs:
            deadline = job.deadline - 1
            if not jobs[deadline]:
                profit += job.profit
                cnt += 1
                jobs[deadline] = True
            else:
                deadline -= 1
                while deadline > -1:
                    if not jobs[deadline]:
                        profit += job.profit
                        cnt += 1
                        jobs[deadline] = True
                        break
                    deadline -= 1

        return cnt, profit
