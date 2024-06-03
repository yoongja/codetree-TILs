n,m = tuple(map(int,input().split()))
a,b = max(n,m), min(n,m)
cnt=a
while(1):
    if cnt%a==0 and cnt%b==0:
        break
    cnt+=1
print(cnt)