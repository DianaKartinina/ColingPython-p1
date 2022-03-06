def solution(x1, y1, x2, y2):
    from math import fabs

    x1 = int(input("Введите координату короля по x "))
    y1 = int(input("Введите координату короля по у "))
    x2 = int(input('Введите координату перемещения по х '))
    y2 = int(input('Введите координату перемещения по у '))
    if x1 and y1 and x2 and y2 > 8:
        print('Это уже не шахматная доска')
    if fabs(x1 - x2) == 1 or fabs(y1 - y2) == 1:
        print("true")
    else:
        print("false")
    return
