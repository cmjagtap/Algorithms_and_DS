from collections import deque
d=deque()
n=int(raw_input())
for i in range(n):
    temp=raw_input().split()
    if temp[0]=="append":
        d.append(int(temp[1]))
    elif temp[0]=="appendleft":
        d.appendleft(int(temp[1]))
    elif temp[0]=="pop":
        d.pop()
    elif temp[0]=="popleft":
        d.popleft()