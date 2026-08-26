"""Arcade of Time: Store Check"""
def arcade():
    """Arcade of Time: Store Check"""
    num = list(map(int, input().split()))
    open_count = [0] * 1441
    for _ in range(num[0]):
        start, stop = map(int, input().split())
        for t in range(start, stop):
            open_count[t] += 1
    time_need = list(map(int, input().split()))
    for n in time_need:
        print(open_count[n], end=" ")
arcade()
