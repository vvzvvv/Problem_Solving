n = int(input())
d = {x:1 for x in input().split()}

m = int(input())
for x in input().split():
    try:
        if d[x]:
            print(1)
    except:
        print(0)