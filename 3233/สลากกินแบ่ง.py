"""สลากกินแบ่ง"""
def main():
    """สลากกินแบ่ง"""
    real_prize = input()
    is_prize = input()
    prize = 0
    if real_prize == is_prize:
        prize = 1000000
    elif is_prize[2:7] == real_prize[2:7] and is_prize[0] != real_prize[0]:
        prize = 100000
    elif is_prize[4:7] == real_prize[4:7] and is_prize[0] == real_prize[0]:
        prize = 2000
    elif is_prize[5:7] == real_prize[5:7] and is_prize[0] == real_prize[0]:
        prize = 1000
    elif is_prize[4:7] == real_prize[4:7] and is_prize[0] != real_prize[0]:
        prize = 200
    elif is_prize[5:7] == real_prize[5:7] and is_prize[0] != real_prize[0]:
        prize = 100
    elif is_prize[0] == real_prize[0] and is_prize[1:7] != real_prize[1:7]:
        prize = 20
    print(prize)
main()
