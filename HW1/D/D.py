def solution(total):
    return ((total // 60) % 24, 'часов' , total % 60 , 'минут')
