from collections import deque
q=deque()
n,m = tuple(map(int,input().split()))
graph=[
    list(map(int,input().split()))
    for i in range(n)
]
visited=[[0 for x in range(m)]for _ in range(n)]

def terr(x,y):
    if x<0 or y<0 or x>m or y>n:
        return False
def can_go(x,y):
    if terr(x,y):
        return True
    if graph[x][y]==0 or visited[x][y]==1:
        return False
    return True
    

dxs,dys=[1,0,-1,0],[0,1,0,-1]
def bfs():
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x,new_y=x+dx,y+dy
            if can_go(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))

q.append((0,0))
bfs()

if visited[-1][-1]:
    print(1)
else:
    print(0)