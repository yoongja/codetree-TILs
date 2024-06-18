import copy

n,m=tuple(map(int,input().split()))

_graph=[
    list(map(int,input().split()))
    for i in range(n)
]

cnt=0
_visited=[[0 for i in range(m)]for i in range(n)]
def can_go(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if visited[x][y] or graph[x][y]==0:
        return False
    return True
    
def dfs(x,y):
    global cnt
    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    for new_x, new_y in zip(dxs,dys):
        new_x+=x
        new_y+=y
        if can_go(new_x,new_y):
            visited[new_x][new_y]=1
            cnt+=1
            dfs(new_x,new_y)
            

def clean(k):
    global cnt
    cnt=0
    graph=copy.deepcopy(_graph)
    visited=copy.deepcopy(_visited)
    for i in range(n):
        for l in range(m):
            if graph[i][l]<=k:
                graph[i][l]=0
    return graph,visited

k=0
for i in _graph:
    sub=max(i)
    k=max(k,sub)

result=[0 for i in range(k)]

for _ in range(1,k+1):
    graph,visited=clean(_)
    for i in range(n):
        cnt=0
        for l in range(m):
            if can_go(i,l):
                visited[i][l]=1
                cnt+=1
            dfs(i,l)
            if cnt!=0:
                result[_-1]+=1
                cnt=0

print(result.index(max(result))+1,max(result))