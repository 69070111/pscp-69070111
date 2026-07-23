"""temp"""
temp = float(input())
temp_now = input()
temp_need = input()
celsius = 0
match temp_now:
    case "C":
        celsius = temp
    case "F":
        celsius = ((temp - 32) * 5) / 9
    case "K":
        celsius = temp - 273.15
    case "R":
        celsius = ((temp * 5) / 9) - 273.15
ans = 0
match temp_need:
    case "C":
        ans = celsius
    case "F":
        ans = ((celsius * 9) / 5) + 32
    case "K":
        ans = celsius + 273.15
    case "R":
        ans = ((celsius + 273.15) * 9) / 5
print(f"{ans:.2f}")
