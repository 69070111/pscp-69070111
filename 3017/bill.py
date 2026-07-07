"""bill"""
price = int(input())
serve = 0.1 * price
if serve < 50:
    serve = 50
if serve > 1000:
    serve = 1000
cal = price + serve
vat = 0.07 * cal
total = cal + vat
print(f"{total:.2f}")
