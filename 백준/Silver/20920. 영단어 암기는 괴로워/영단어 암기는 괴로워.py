from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [word for word in (input() for _ in range(n)) if len(word) >= m]

counter = Counter(arr)
arr = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, num in arr:
    print(word)