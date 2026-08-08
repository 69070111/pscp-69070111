"""ให้หาว่ามีจำนวนนับxกี่ตัวในช่วงa,bที่หารด้วยdและเหลือเศษr"""
num_a = int(input())
num_b = int(input())
divine_d = int(input())
fraction_r = int(input())
check = 0

for i in range(num_a, num_b + 1):
    if i % divine_d == fraction_r:
        check += 1
print(check)
