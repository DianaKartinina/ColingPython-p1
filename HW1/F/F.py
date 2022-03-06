def solution(n):
    import math
    num = int(input('Введите число '))
    step = 0
    if 2 > num:
       print("Нет решения")

    for i in range(num):
       x = pow(2, step)
       step += 1
       print(x)
    if x >= num:
        break
    return
