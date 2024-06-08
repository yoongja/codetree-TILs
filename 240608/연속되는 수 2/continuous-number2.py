n= int(input())
cnt=0
result=[]
for i in range(n):
    if i==0:
        x=int(input())
        continue
    sub=int(input())
    if x!=sub:
        result.append(cnt)
        cnt=0
    else:
        cnt+=1
    x=sub
print(max(result)+1)