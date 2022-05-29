import math
def solution(n):
    lst = []
    st = 1
    while st <= n:
        lst.append(st)
         st = st * 2
    return lst
