"""ของขวัญและขโมย"""
def gift_and_thief():
    """ของขวัญและขโมย"""
    n, k, t = map(int, input().split())
    check, check_ans = 1, 0
    while True:
        if check == t:
            check_ans += 1
            break
        check += k
        if check > n:
            check -= n
        check_ans += 1
        if check == 1:
            break
    print(check_ans)
gift_and_thief()
