"""หาว่าใช้สะพานสร้างต้องใช้เท่าไหร่"""
num_a = int(input())
num_b = int(input())
goal = int(input())
cal1 = min(goal // 5, num_b)
howmuch = goal - (cal1 * 5)
if num_a >= howmuch:
    print(howmuch)
elif num_a < howmuch:
    print(-1)
