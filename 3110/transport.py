"""ระบส่งของ"""
ton, pray = input().split()
weight = float(input())
if ton == "BKK" and pray == "CNX":
    print(f"{(weight * 30) + 10:.2f}")
elif ton == "CNX" and pray == "UBP":
    print(f"{(weight * 40) + 15:.2f}")
elif ton == "UBP" and pray == "BKK":
    print(f"{(weight * 40) + 20:.2f}")
elif ton == "BKK" and pray == "PKT":
    print(f"{(weight * 50) + 25:.2f}")
elif ton == "PKT" and pray == "CNX":
    print(f"{(weight * 60) + 30:.2f}")
elif ton == "UBP" and pray == "PKT":
    print(f"{(weight * 70) + 40:.2f}")
else:
    print("Error")
