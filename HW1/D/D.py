def solution(total):
    n = int(input('Введите число '))
    print(n % (60 * 24) // 60, 'часов' , n % 60 , 'минут')
    return
