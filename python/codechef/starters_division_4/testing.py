# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict.fromkeys(range(40), 0)
    for i in a:
        c = 0
        t = i
        while t >= 2:
            t = t / 2
            c += 1
        d[c] += 1
    print(d)
    # s = 0
    # for i in range(40):
    #     s = (d[i]*(d[i]-1))//2 + s
    # print(s)
