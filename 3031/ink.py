"""บอกว่าน้ำของคนที่ถามจะท่วมตอนไหน"""
import math
def ink():
    """ฟังก์ชั่นบอกว่าน้ำของคนที่ถามจะท่วมตอนไหน"""
    ink_s, people_n = input().split()
    for _ in range(int(people_n)):
        x_i, y_i = input().split()
        area = 3.1416 * ((int(x_i) ** 2) + (int(y_i) ** 2))
        time = area / int(ink_s)
        print(math.ceil(time))
ink()
