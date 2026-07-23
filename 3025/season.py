"""season"""
month = int(input())
days = int(input())
if month in (1, 2, 3):
    if days >= 21 and not month % 3:
        print("spring")
    else:
        print("winter")

elif month in (4, 5, 6):
    if days >= 21 and not month % 3:
        print("summer")
    else:
        print("spring")

elif month in (7, 8, 9):
    if days >= 21 and not month % 3:
        print("fall")
    else:
        print("summer")

elif month in (10, 11, 12):
    if days >= 21 and not month % 3:
        print("winter")
    else:
        print("fall")
