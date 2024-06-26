import sys
import copy
from collections import deque
## sys.exit() 디버깅 아예종료
## sys.maxsize = 정수 최대값

q = deque()
n,k = map(int,input().split())

graph=[list(map(int,input().split()))
       for i in range(n)]

start_point=[tuple(map(int,input().split()))
             for l in range(k)]

visited = [[False for _ in range(n)] for __ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and graph[x][y]==0


def bfs():
    cnt=0
    while q:
        x,y = q.popleft()
        dxs, dys =[1,0,-1,0,0],[0,1,0,-1,0]
        for dx, dy in zip(dxs,dys):
            dx,dy= dx+x,dy+y
            if can_go(dx,dy):
                q.append((dx,dy))
                visited[dx][dy]=True
                cnt+=1
    return cnt

cnt=0

for i in range(len(start_point)):
    x,y=start_point[i]
    q.append((x-1,y-1))
    cnt+=bfs()
print(cnt)