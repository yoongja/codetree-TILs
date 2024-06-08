import sys
n= int(input())
if n==1:
    print(1)
    sys.exit()

cnt_l=0
cnt_r=0
result=[]
for i in range(n):
    x=int(input())
    if x<0:
        if cnt_l==0:
            result.append(cnt_r)
            cnt_r=0
        cnt_l+=1
    elif x>0:
        if cnt_r==0:
            result.append(cnt_l)
            cnt_l=0
        cnt_r+=1
result.append(cnt_l)
result.append(cnt_r)
print(max(result))