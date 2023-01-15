# Задача №3.
# Написать метод zeros, который принимает на вход целое число (integer) 
# и возвращает количество конечных нулей в факториале 
# (N! = 1 * 2 * 3 * ... * N) заданного числа:

# Будьте осторожны 1000! имеет 2568 цифр.

# Доп. инфо: http://mathworld.wolfram.com/Factorial.html

# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros

# Основа:
# def zeros(n):
#     return 0

# Подсказка: вы не должны вычислять факториал. Найдите другой способ 
# найти количество нулей.

# Для проверки:
# assert zeros(0) == 0
# assert zeros(6) == 1
# assert zeros(30) == 7
# -----------------------------------------------------------------------------


# Решение задачи:

def zeros(n):

    countZero = 0

    while n/5 > 1:
        n = n/5
        countZero += n

    return int(countZero)

    # Либо можно через рекурсию, в одну строчку:
    # return 0 if int(n/5) < 1 else int(n/5) + int(zeros(n/5))

# Проверка:

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(12) == 2
assert zeros(30) == 7
assert zeros(1000) == 249

# Всё ОК!