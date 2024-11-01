import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

k, n = map(int, input().split())
nums = []

def recur(cnt):
    if cnt == n:
        for num in nums:
            print(num)
        return

    for i in range(1, k + 1):
 
        if cnt >= 2 and i == selected_nums[-1] and i == selected_nums[-2]:
            continue

        else:
            nums.append(i)
            recur(cnt+1)
            nums.pop()
recur(0)