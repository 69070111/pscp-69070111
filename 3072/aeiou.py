"""นับว่าสระมีกี่ตัว"""
def sara(text):
    """ฟังก์ชั่นนับสระว่ามีกี่ตัว"""
    vowel = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for char in text:
        if char in vowel:
            vowel[char] += 1
    for i, count in vowel.items():
        if count > 0:
            print(f"{i} : {count}")
sara(input().lower())
