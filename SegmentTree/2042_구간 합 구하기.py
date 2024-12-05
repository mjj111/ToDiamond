import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
tree = [0] * (4*N)

def build(x, left, right) :
    if left == right:
        tree[x] = numbers[left]
        return tree[x]

    mid = (left + right) // 2
    right = build(2*x + 1, mid+1, right);
    left = build(2*x, left, mid);

    tree[x] = right + left
    return tree[x]

build(1, 0, N-1)

def find(x, left, right, start, end) :
    if end < left or start > right: return 0
    if start <= left and end >= right: return tree[x]

    mid = (left + right) // 2
    left = find(2*x, left, mid, start, end)
    right = find(2*x + 1, mid + 1, right, start, end)
    return right + left

def update(x, left, right, index, value) :
    if left == right == index:
        tree[x] = value
        return
    if index < left or index > right :
        return

    mid = (left + right) // 2
    update(2*x, left, mid, index, value)
    update(2*x+1, mid+1, right, index, value)

    tree[x] = tree[2*x] + tree[2*x+1]

for _ in range(M+K):
    a,b,c = map(int,input().split())

    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(find(1, 0, N-1, b-1, c-1))