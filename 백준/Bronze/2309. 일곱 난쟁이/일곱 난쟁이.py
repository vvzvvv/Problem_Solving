lst = []
for _ in range(9):
    lst.append(int(input()))
total = sum(lst)

flag = True
for i in range(0, len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if total - (lst[i] + lst[j]) == 100:
            lst.pop(j)
            lst.pop(i)
            flag = False
            break
    if not flag: break

lst.sort()
for l in lst:
    print(l)