"""สลับที่ตัวอักษร"""
while True:
    text = input()
    if len(text) <= 5:
        break
print(text[::-1].lower())
