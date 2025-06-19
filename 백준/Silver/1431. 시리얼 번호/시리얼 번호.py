n = int(input())
arr = [input() for _ in range(n)]

def sum_of_digits(word):
    return sum(int(ch) for ch in word if ch.isdigit())

arr.sort(key=lambda x:(
    len(x),
    sum_of_digits(x),
    x
    ))
for a in arr:
    print(a)