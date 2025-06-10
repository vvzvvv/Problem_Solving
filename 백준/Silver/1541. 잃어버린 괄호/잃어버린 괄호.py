lst = list(input().split("-"))

total = sum(list(map(int, lst[0].split("+"))))
for i in range(1, len(lst)):
    for num in lst[i].split("+"):
        total -= int(num)

print(total)