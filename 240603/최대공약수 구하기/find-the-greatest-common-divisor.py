n,m = tuple(map(int,input().split()))
a,b = max(n,m), min(n,m)
cnt=b
while(1):
    if a%cnt==0 and b%cnt==0:
        break
    cnt-=1
print(cnt)