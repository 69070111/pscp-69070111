"""หาว่าจำนวนกำแพงที่จะไปโดยผ่านกำแพงน้อยที่สุดให้ไปหาเข1ได้"""
import math
def castle():
    """หาว่าจะต้องใช้กี่กำแพงให้น้อยที่สุดถึงจะไปถึงห้องเลข1ได้"""
    num = int(input())
    row = math.ceil(math.sqrt(num))
    is_upside_down = (not row % 2 and num % 2) or (row % 2 and not num % 2)
    if num == 1:
        print(0)
    elif is_upside_down:
        print(((row - 1) * 2) - 1)
    else:
        print((row - 1) * 2)
castle()
