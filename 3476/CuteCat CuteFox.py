"""CuteCat CuteFox"""
import ast
def catfox():
    """CuteCat CuteFox"""
    n = int(input().strip())

    herd = {}
    count = 0
    while count < n:
        line = input().strip()
        if not line:
            continue
        d = ast.literal_eval(line)
        for name, num in d.items():
            herd[num.strip()] = name.strip()
        count += 1

    if "Cat01" not in herd and "Garfield" not in herd.values():
        herd["Cat01"] = "Garfield"
    if "Fox01" not in herd and "Fubuki" not in herd.values():
        herd["Fox01"] = "Fubuki"

    def number(code):
        return int(code[3:])

    cats = sorted((c for c in herd if c.startswith("Cat")), key=number)
    foxes = sorted((f for f in herd if f.startswith("Fox")), key=number)

    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for code in cats + foxes:
        print(herd[code], ":", code)
catfox()
