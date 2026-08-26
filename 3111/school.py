"""คำนวนหาส่วนลดขนมและเครื่องดื่ม"""
from math import ceil
def school():
    """main"""
    m = input().upper()
    n_howmany = int(input())
    howmuch_count = 0

    for _ in range(n_howmany):
        howmuch = float(input())
        howmuch_count += howmuch

    if m == "Y":
        total = howmuch_count - (howmuch_count * 0.05)
    elif m == "N" and howmuch_count >= 500:
        total = howmuch_count - (howmuch_count * 0.03)
    else:
        total = howmuch_count
    print(f"{(ceil(total * 100) / 100):.2f}")
school()
