# TasksPython
## Три задачки по Python


### Задача №1
Написать метод domain_name, который вернет домен из url адреса:

url = "http://github.com/carbonfive/raygun" -> domain name = "github"  
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"  
url = "https://www.cnet.com"                -> domain name = "cnet"  
  
Основа:  
def domain_name(url):  
  return  
  
Для проверки:  
assert domain_name("http://google.com") == "google"  
assert domain_name("http://google.co.jp") == "google"  
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"  


### Задача №2
Написать метод int32_to_ip, который принимает на вход 32-битное целое число   
(integer) и возвращает строковое представление его в виде IPv4-адреса:  
  
2149583361 -> "128.32.10.1"  
32         -> "0.0.0.32"  
0          -> "0.0.0.0"  
  
Основа:  
def int32_to_ip(int32):  
  return  
  
Для проверки:  
assert int32_to_ip(2154959208) == "128.114.17.104"  
assert int32_to_ip(0) == "0.0.0.0"  
assert int32_to_ip(2149583361) == "128.32.10.1"  


### Задача №3
Написать метод zeros, который принимает на вход целое число (integer)   
и возвращает количество конечных нулей в факториале  
(N! = 1 * 2 * 3 * ... * N) заданного числа:  

Будьте осторожны 1000! имеет 2568 цифр.  
  
Доп. инфо: http://mathworld.wolfram.com/Factorial.html  
  
zeros(6) = 1  
(6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero)  
  
zeros(12) = 2  
(12! = 479001600 --> 2 trailing zeros)  
  
Основа:  
def zeros(n):  
    return 0  
  
Подсказка: вы не должны вычислять факториал. Найдите другой способ   
найти количество нулей.  
  
Для проверки:  
assert zeros(0) == 0  
assert zeros(6) == 1  
assert zeros(30) == 7  

