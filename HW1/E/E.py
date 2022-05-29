def solution(x1, y1, x2, y2):
    from math import fabs
    if x1 and y1 and x2 and y2 > 8:
        return('Это уже не шахматная доска')
    if fabs(x1 - x2) == 1 or fabs(y1 - y2) == 1:
        return("true")
    else:
        return("false")

