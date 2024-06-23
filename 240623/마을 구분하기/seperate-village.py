n=int(input())
graph=[
    list(map(int,input().split()))
    for i in range(n)
]
visited=[[0 for _ in range(n)]for i in range(n)]
cnt=0
def can_go(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    return True

def visit(x,y):
    if can_go(x,y)==False:
        return False
    elif visited[x][y] or graph[x][y]==0:
        return False
    return True

def dfs(x,y):
    global cnt
    if x==0 and y==0:
        if visit(x,y):
            cnt+=1
    dxs,dys=[1,0,-1,0],[0,1,0,-1]
    for dx, dy in zip(dxs,dys):
        new_x,new_y=x+dx,y+dy
        if visit(new_x,new_y):
            visited[new_x][new_y]=1
            graph[x][y]=0
            cnt+=1
            dfs(new_x,new_y)
result=[]
for i in range(n):
    for l in range(n):
        dfs(i,l)
        if cnt>=1:
            result.append(cnt)
            cnt=0
            
print(len(result))
result.sort()
for i in result:
    print(i)