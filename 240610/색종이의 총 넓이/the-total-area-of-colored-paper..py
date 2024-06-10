off=100
M=200
graph=[[0 for i in range(M)]for l in range(M)]
lst=[]

n=int(input())
for i in range(n):
    x,y=tuple(map(int,input().split()))
    lst.append((x+off,y+off))
cnt=0
for x,y in lst:
    for i in range(x,x+8):
        for l in range(y,y+8):
            if graph[i][l]==1:
                continue
            else:
                graph[i][l]=1
                cnt+=1
print(cnt)