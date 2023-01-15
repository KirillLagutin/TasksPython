# Задача №1.
# Написать метод domain_name, который вернет домен из url адреса:

# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"

# Основа:
# def domain_name(url):
#   return

# Для проверки:
# assert domain_name("http://google.com") == "google"
# assert domain_name("http://google.co.jp") == "google"
# assert domain_name("www.xakep.ru") == "xakep"
# assert domain_name("https://youtube.com") == "youtube"
# -----------------------------------------------------------------------------


# Решение задачи:

def domain_name(url):

    domain = url.split('.')

    if domain[0].find('www') != -1:
        domain = domain[1].split('.')
        return domain[0]

    elif domain[0].find('//') != -1:
        domain = domain[0].split('//')
        return domain[1]

    else:
        return domain[0]

# Проверка:

assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("https://www.xakep.ru") == "xakep"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("youtube.com") == "youtube"

# Всё ОК!