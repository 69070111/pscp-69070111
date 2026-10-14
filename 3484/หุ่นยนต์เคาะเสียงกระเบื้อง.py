"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
def mech():
    """หุ่นยนต์เคาะเสียงกระเบื้อง"""
    n, p = input().split()
    n = int(n)
    p = float(p)

    grid = []
    for _ in range(n):
        line = input().split()
        while not line:
            line = input().split()
        grid.append(list(map(int, line)))

    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0

    for i in range(n):
        row_tiles = 0
        row_points = 0
        for j in range(n):
            x = grid[i][j]
            if x > 0:
                row_tiles += 1
                col_tiles[j] += 1
            row_points += x
            col_points[j] += x
        total_tiles += row_tiles
        total_points += row_points
        print(*grid[i], row_tiles, row_points)

    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
mech()
