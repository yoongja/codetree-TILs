n = int(input())
arr = list(map(int, input().split()))

ans = 0
#구간은 1부터 n까지의 경우의 수를 가진다
for i in range(1, n+1): #i 만큼의 크기가 구간의 크기
    #print("구간크기", i) # 구간의 크기가 i일때
    for j in range(n-i+1):
        now = arr[j:j+i]
        #print(now)
        tmp_avg = sum(now)//i 
        #print(tmp_avg)

        for n in now:
            if n == tmp_avg:
                ans += 1
                break
print(ans)