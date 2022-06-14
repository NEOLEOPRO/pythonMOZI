import math
import numpy as np


def gcd(a, b):
    """Вычисление обратной матрицы ключа"""
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def reverse(key, alph, n):
    """Вычисление обратной матрицы ключа"""
    key_r = np.linalg.inv(key)
    det = round(np.linalg.det(key))
    key_r = np.round(key_r * det)
    x, y, a = gcd(len(alph), round(det) % len(alph))
    key_r *= y
    key_r = np.round(key_r) % len(alph)
    key_r = key_r.reshape(1, n * n)
    h = str(list(map(int, list(key_r)[0])))[1:-1].replace(',', '')
    key_r = np.array(list(map(int, h.split(' '))))
    key_r = key_r.reshape(n, n)

    return key_r


def hill_encode(text, alph, key):
    """Часть отвечающая за шифрование стандартным шифром"""
    n = len(key)
    return new(text, n, alph, key)


def new(text, n, alph, key):
    """Получение сообщения или шифротекста примерением к нему ключа обратного или обычного"""
    ans = ''
    for i in range(0, len(text), n):
        x = []
        k = i
        while k < i + n:
            x.append(alph.find(text[k]))
            k += 1
        x = np.array(x).reshape(n, 1)
        y = key.dot(x) % 29
        y = list(y.reshape(1, n))
        for j in y[0]:
            ans += alph[j]
    return ans


def hill_decode(text, alph, key):
    """Часть отвечающая за расшифрование стандартным шифром"""
    n = len(key)
    key_r = reverse(key, alph, n)

    return new(text, n, alph, key_r)


def req_hill_encode(text, alph, key1, key2):
    """Часть отвечающая за шифрование рекуррентным шифром"""
    n = len(key1)
    ans = ''
    count = 1
    for i in range(0, len(text), n):
        x = []
        k = i
        if count == 1 or count == 2:
            while k < i + n:
                x.append(alph.find(text[k]))
                k += 1
            x = np.array(x).reshape(n, 1)
            y = key1.dot(x) % 29
            y = list(y.reshape(1, n))
            for j in y[0]:
                ans += alph[j]
            count += 1
        else:
            key = key2.dot(key1)
            while k < i + n:
                x.append(alph.find(text[k]))
                k += 1
            x = np.array(x).reshape(n, 1)
            y = key.dot(x) % 29
            y = list(y.reshape(1, n))
            for j in y[0]:
                ans += alph[j]
            key2, key1 = key.copy(), key2.copy()
            count += 1
    return ans


def req_hill_decode(text, alph, key1, key2):
    """Часть отвечающая за расшифрование рекуррентным шифром по сути шифрование но с обратными ключами"""
    n = len(key1)
    key1 = reverse(key1, alph, n)
    key2 = reverse(key2, alph, n)
    ans = req_hill_encode(text, alph, key1, key2)
    return ans


def main():
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?'.lower()
    print("Выберите вариацию шифра Хилла:")
    print("1 - Обычный")
    print("2 - Реккурентный")
    type_of_cipher = int(input())
    if type_of_cipher < 1 or type_of_cipher > 2:
        raise TypeError("Неверный вариант")

    print("Выберите действие")
    print("1 - Зашифрование")
    print("2 - Расшифрование")
    crypt_decrypt = int(input())
    if crypt_decrypt < 1 or crypt_decrypt > 2:
        raise TypeError("Неверный вариант")


    print('Введите размер матрицы 2 или 3')
    size = int(input())
    if size < 2 or size > 3:
        raise TypeError("Неверный вариант")

    text = str(input('Введите сообщение:')).lower()
    while len(text) % size != 0:
        text += 'a'

    print('Введите ключ-матрицу после примера:')
    print('Пример:')
    print('1 0 0')
    print('0 1 0')
    print('0 0 1')
    print('')
    key = list()
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            raise TypeError('Неправильный размер матрицы')
        key.append(row)
    key = np.array(key)
    if math.gcd(int(np.linalg.det(key)), len(alph)) != 1 or int(np.linalg.det(key)) == 0:
        raise TypeError('Неверный ключ')

    if type_of_cipher == 1:
        if crypt_decrypt == 1:
            print('Шифртекст:', hill_encode(text, alph, key))
        else:
            print('Открытый текст:', hill_decode(text, alph, key))
    else:
        print('Введите второй ключ-матрицу после примера:')
        print('Пример:')
        print('1 0 0')
        print('0 1 0')
        print('0 0 1')
        print('')

        key2 = list()
        for i in range(size):
            row = list(map(int, input().split()))
            if len(row) != size:
                raise TypeError('Неправильной длины ключ')
            key2.append(row)
        key2 = np.array(key)
        if math.gcd(int(np.linalg.det(key2)), len(alph)) != 1 or int(np.linalg.det(key2)) == 0:
            raise TypeError('Неверный ключ')

        if crypt_decrypt == 1:
            print('Шифртекст:', req_hill_encode(text, alph, key, key2))
        else:
            print('Открытый текст:', req_hill_decode( text, alph, key, key2))


if __name__ == '__main__':
    main()