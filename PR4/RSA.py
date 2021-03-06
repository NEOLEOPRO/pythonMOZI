"""coded dy wiskas(github)"""

import random
from random import randint


def get_binary_map(k):
    kmap = list()
    while k != 0:
        kmap.append(k % 2)
        k = k // 2
    return kmap


def fast_degree(a, k):
    if k == 0:
        return 1
    if k == 1:
        return a

    kmap = get_binary_map(k)
    base_deg = a
    if kmap[0] == 1:
        res = a
    else:
        res = 1
    for deg in kmap[1:]:
        base_deg *= base_deg
        if deg == 1:
            res *= base_deg
    return res


def test_ferma(a):
    for i in range(20):
        m = randint(2, a - 1)
        r = pow(m, a - 1, a)
        if r != 1:
            return False
    return True


def get_random_prime(len):
    res = 4
    while not test_ferma(res):
        res = random.getrandbits(len)
    return res


def evklid(a, b):
    if b > a:
        raise Exception("a should be bigger than b")
    x1, x2, y1, y2 = 0, 1, 1, 0
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
    d, x, y = a, x2, y2
    return d, x, y


def reciprocal_number(a, n):
    d, x, y = evklid(n, a)
    if d != 1:
        raise Exception("d != 1 (" + str(d) + ")")
    if y < 0:
        y += n
    return y


def get_coprime(start, end, n):
    res = n
    d, x, y = evklid(n, res)
    while d != 1:
        res = randint(start, min(end, n))
        d, x, y = evklid(n, res)
    return res


def generate_keys():
    p = get_random_prime(1000)
    q = get_random_prime(1000)
    f = (p - 1) * (q - 1)
    e = get_coprime(random.getrandbits(100), random.getrandbits(1000), f)
    d = reciprocal_number(e, f)
    n = p * q
    print("p:", p, '\n', "q:", q)
    return e, d, n


def keygen():
    text = "n"
    while text != "":
        e, d, n = generate_keys()
        print("Текущие ключи:")
        print("Зашифрования: e=" + str(e) + ",\nn=" + str(n) + ")")
        print("Расшифрования: d=" + str(d) + ",\nn=" + str(n) + ")")
        text = input("Использовать данные ключи? Enter-подтвердить")
    return e, d, n


def keyinput():
    text = "n"
    while text != "":
        e = int(input("Введите первый ключ шифрования: "))
        d = int(input("Введите первый ключ дешифрования: "))
        n = int(input("ВВедите второй ключ шифрования и дешифрования: "))
        print("Текущие ключи:")
        print("Зашифрования: (" + str(e) + ", " + str(n) + ")")
        print("Расшифрования: (" + str(d) + ", " + str(n) + ")")
        print("Сохранить ключи? Enter-подтвердить")
        text = input()
    return e, d, n


def encrypt(e, n):
    print("Ключ зашифрования: (" + str(e) + ", " + str(n) + ")")
    message = input("Введите исходное сообщение (на английском): ")
    numbers = [to_num[i] for i in message]
    numbers = [pow(i, e, n) for i in numbers]
    print("Зашифрованное сообщение:")
    print(numbers)
    input("нажмине Enter чтобы продолжить")
    return message, numbers


def decrypt(numbers, d, n):
    print("Ключ расшифрования: (" + str(d) + ", " + str(n) + ")")
    print("Зашифрованное сообщение:")
    print(numbers)
    message = decrypt(numbers, d, n)
    numbers = [pow(i, d, n) for i in numbers]
    message = [to_sym[i] for i in numbers]
    message = "".join(message)
    print("Расшифрованнное сообщение:")
    print(message)
    input("нажмине Enter чтобы продолжить")
    return message


def notar(numbers, e, d, n):
    print("Известные данные:")
    print("Открытый ключ зашифрования: (" + str(e) + ", " + str(n) + ")")
    print("Зашифрованное сообщение:")
    print(numbers)
    print("Создание взаимнопростой с n переменнной r:")
    r = get_coprime(1000, 10000, n)
    print("r =", r)
    print("Создание обратной к r по модулю n переменной t:")
    t = reciprocal_number(r, n)
    print("t =", t)
    print("Зашфрование переменной r по известному открытому ключу: ")
    x = pow(r, e, n)
    print("x =", x)
    print("Изменение шифртекста с помощью умножения каждого элемента на x: ")
    y = [(x * i) % n for i in c]
    print(y)
    print()
    print("Расшифровка сообщения другим пользователем, имеющим ключ расшифрования: ")
    w = [pow(i, d, n) for i in y]
    print(w)
    print()
    print("Изменение ""Расшифырованного"" текста с помощью домножения каждого элемента на t: ")
    y = [(i * t) % n for i in w]
    print(y)
    print("Преобразование в символы: ")
    y = [to_sym[i] for i in y]
    message = "".join(y)
    print(message)
    input("нажмине Enter чтобы продолжить")
    return message




to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
          "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
          "z": 25}

to_sym = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m",
          13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y",
          25: "z"}

if __name__ == "__main__":
    e, d, n = 0, 0, 0
    c, m = "", ""
    while True:
        print("1)Генерация ключей")
        print("2)Ввод ключей")
        print("3)Зашифровка сообщения")
        print("4)Расшифровка сообщения")
        print("5)Атака схемы с нотариусом")
        print("Выберите действие:")
        num = input()
        if num == "1":
            e, d, n = keygen()
        if num == "2":
            e, d, n = keyinput()
        if num == "3":
            if n != 0:
                m, c = encrypt(e, n)
            else:
                print("Для зашифровки сгенерируйте или введите ключи!")
        if num == "4":
            if c != "":
                m1 = decrypt(c, d, n)
            else:
                print("Для расшифровки зашифруйте сообщение!")
        if num == "5":
            if c != "":
                m2 = notar(c, e, d, n)
            else:
                print("Для проведения атаки схемы с нотариусом зашифруйте сообщение!")
        if num == "0":
            break
