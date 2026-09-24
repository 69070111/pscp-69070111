"""กบน้อยกระโดด"""
def frog_jump():
    """กบน้อยกระโดด"""
    x, y = map(int, input().split())
    total_distance = 0
    total_jump = 0
    while True:
        total_distance += x
        x -= 2
        total_jump += 1
        if total_distance >= y:
            break
        if x <= 0:
            break
    if total_distance < y:
        total_jump = -1
    print(total_jump)
frog_jump()
