"""BigFrame"""
def frame():
    """BigFrame"""
    text_list = []
    text_list2 = []
    for _ in range(5):
        text = input()
        text_len = len(text.strip())
        text_list2.append(text.strip())
        text_list.append(text_len)
    text_max = max(text_list)
    print("*" * (text_max + 4))
    for i in text_list2:
        space_left = text_max - len(i)
        hell_nah = i + (space_left * " ")
        print(f"* {hell_nah} *")
    print("*" * (text_max + 4))
frame()
