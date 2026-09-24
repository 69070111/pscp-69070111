"""แปลงดอกไม้"""
def flower():
    """แปลงดอกไม้"""
    l, n = map(int, input().split())
    row = 0
    cross = 0
    first_row = l * (l + 1) // 2
    while cross < n:
        row += 1
        cross += first_row + (row - 1) * (l ** 2)
    print(row)
flower()
