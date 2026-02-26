import sys
input = sys.stdin.readline

deq = [0] * 20001
head = 10000
tail = 10000

def push_front(x):
    global head
    head -= 1
    deq[head] = x
    
def push_back(x):
    global tail
    deq[tail] = x
    tail += 1

def pop_front():
    global head
    global tail
    
    if head == tail:
        return -1
    else:
        result = deq[head]
        head += 1
        return result
    
def pop_back():
    global head
    global tail
    
    if head == tail:
        return -1
    else:
        tail -= 1
        result = deq[tail]
        return result

def size():
    global head
    global tail
    
    return tail - head

def empty():
    global head
    global tail
    
    if head == tail:
        return 1
    else:
        return 0

def front():
    global head
    global tail
    
    if head == tail:
        return -1
    else:
        return deq[head]
        
def back():
    global head
    global tail
    
    if head == tail:
        return -1
    else:
        return deq[tail - 1]

# === #

n = int(input())

for _ in range(n):
    line = input().split()
    com = line[0]
    
    if len(line) == 2:
        num = int(line[1])
        print_ = globals()[com](num)
    else:
        print_ = globals()[com]()
        
    if print_ != None:
        print(print_)