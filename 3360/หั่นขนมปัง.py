"""หั่นขนมปัง"""
def cut_bread():
    """หั่นขนมปัง"""
    w, h, _, _ = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    px = [0] + xs + [w]
    widths = [px[i + 1] - px[i] for i in range(len(px) - 1)]

    py = [0] + ys + [h]
    heights = [py[i + 1] - py[i] for i in range(len(py) - 1)]

    widths.sort(reverse=True)
    heights.sort(reverse=True)

    first = widths[0] * heights[0]
    second = max(widths[0] * heights[1], widths[1] * heights[0])

    print(first, second)
cut_bread()
