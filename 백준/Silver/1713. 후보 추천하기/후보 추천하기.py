n = int(input()) # 사진틀 수
total = int(input()) # 총 추천 횟수
arr = list(map(int, input().split()))

result = []
cnt = [1001] * 101
for nominate in arr:
    if nominate in result:
        cnt[nominate] += 1
    else:
        if len(result) >= n: # 틀 다 참
            min_value = min(cnt)
            for i in range(n):
                if cnt[result[i]] == min_value:
                    cnt[result[i]] = 1001
                    result.remove(result[i])
                    break
                
        cnt[nominate] = 1   
        result.append(nominate)

print(*sorted(result))
