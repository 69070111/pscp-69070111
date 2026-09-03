"""เกมสะสมแต้ม"""
def game():
    """เกมสะสมแต้ม"""
    numbers = int(input())
    count = 0
    for _ in range(numbers):
        mark = input()
        if mark == "+":
            count += 10
        elif mark == "-":
            count -= 5
    print(count)
game()
