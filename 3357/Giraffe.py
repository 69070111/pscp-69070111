"""Giraffe"""
def giraffe():
    """Giraffe"""
    n = int(input())
    heights = []
    for _ in range(n):
        heights.append(int(input()))

    count = 0
    if n == 1:
        count = 1
    else:
        for i in range(n):
            if not i and heights[0] > heights[1]:
                count += 1

            elif i == n - 1:
                if heights[i] > heights[i - 1]:
                    count += 1

            else:
                if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
                    count += 1

    print(count)
giraffe()
