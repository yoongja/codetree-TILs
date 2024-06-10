offset=1000
M=2000
graph=[[0 for i in range(M)]for l in range(M)]

lst=[]
for i in range(3):
    lst.append(tuple(map(int,input().split())))

cnt=1
erase,add=0,0
for a,b,c,d in lst:
    a,b,c,d = a+offset, b+offset, c+offset, d+offset
    if cnt==3:
        for x in range(a,c):
            for y in range(b,d):
                if graph[x][y]==1:
                    erase+=1
    else:
        for x in range(a,c):
            for y in range(b,d):
                add+=1
                graph[x][y]=1
    cnt+=1
print(add-erase)