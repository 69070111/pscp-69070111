"""ส่งต่อ"""
def send():
    """ส่งต่อ"""
    n, s = map(int, input().split())

    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        nxt[i] = int(input())

    visited = [False] * (n + 1)
    count = 0
    cur = s

    while cur and not visited[cur]:
        visited[cur] = True
        count += 1
        cur = nxt[cur]

    print(count)
send()
