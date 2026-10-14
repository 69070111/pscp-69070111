"""Duplicate I"""


def dup():
    """Duplicate I"""
    m = int(input())
    n = int(input())
    list_student_m = []
    list_student_n = []
    check = []
    for _ in range(m):
        student_m = int(input())
        list_student_m.append(student_m)
    for _ in range(n):
        student_n = int(input())
        list_student_n.append(student_n)
    for _, student in enumerate(list_student_m):
        if student in list_student_n:
            check.append(student)

    if not check:
        print("Nope")
    else:
        for i in sorted(set(check), reverse=True):
            print(i)
dup()
