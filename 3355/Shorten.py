"""Shorten"""
def shorten():
    """Shorten"""
    nums = []
    while True:
        n = int(input())
        if n == -1:
            break
        nums.append(n)

    if not nums:
        print()
    else:
        result = []
        start = nums[0]
        prev = nums[0]

        for x in nums[1:]:
            if x == prev + 1:
                prev = x
            else:
                if start == prev:
                    result.append(str(start))
                else:
                    result.append(str(start) + "-" + str(prev))
                start = x
                prev = x

        if start == prev:
            result.append(str(start))
        else:
            result.append(str(start) + "-" + str(prev))

        print(", ".join(result))
shorten()
