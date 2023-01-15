# Задача №2.
# Написать метод int32_to_ip, который принимает на вход 32-битное целое число 
# (integer) и возвращает строковое представление его в виде IPv4-адреса:

# 2149583361 -> "128.32.10.1"
# 32         -> "0.0.0.32"
# 0          -> "0.0.0.0"

# Основа:
# def int32_to_ip(int32):
#   return

# Для проверки:
# assert int32_to_ip(2154959208) == "128.114.17.104"
# assert int32_to_ip(0) == "0.0.0.0"
# assert int32_to_ip(2149583361) == "128.32.10.1"
# -----------------------------------------------------------------------------


# Решение задачи:

def int32_to_ip(int32):
    
    temp = 256
    temp2 = 256*256
    temp3 = 256*256*256

    octet1 = int(int32/temp3)
    octet2 = int((int32 - octet1*temp3) / temp2)
    octet3 = int((int32 - octet1*temp3 - octet2*temp2) / temp)
    octet4 = int(int32 - octet1*temp3 - octet2*temp2 - octet3*temp)

    return f"{octet1}.{octet2}.{octet3}.{octet4}"

# Проверка:

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

# Всё ОК!