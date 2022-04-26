def affine(p: str, k11: int, k12: int, k21: int, k22: int):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !?.,():"
    c = ""
    ii = 0
    if gcd(k11) != 1:
        print("Warning: k11 первой пары не взаимно простой с 34, дешифрование с данным ключём не получится")
    if gcd(k21) != 1:
        print("Warning: k21 второй пары не взаимно простой с 34, дешифрование с данным ключём не получится")
    for i in p:
        if i in alf:
            if ii == 0:
                c += alf[(alf.find(i) * k11 + k12) % 34]
                ii += 1
                continue
            c += alf[(alf.find(i) * k21 + k22) % 34]
            k11, k21 = k21, k11 * k21
            k12, k22 = k22, k12 + k22
        else:
            c += i
    return c


def gcd(x: int, y=34):
    s = 1
    if x > y:
        temp = y
    else:
        temp = x
    for i in range(1, temp + 1):
        if (x % i == 0) and (y % i == 0):
            s = i
    return s


def decode(p: str, k11: int, k12: int, k21: int, k22: int):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!?.,() "
    c1 = ""
    ii = 0
    k11_re = 1
    k21_re = 1
    if gcd(k11) != 1:
        return "Error: k11 первой пары не взаимно простой с 34"
    if gcd(k21) != 1:
        return "Error: k21 второй пары не взаимно простой с 34"
    for i in p:
        if i in alf:
            for a in range(34):
                if (k11 * a) % 34 == 1:
                    k11_re = a
                    break
            for b in range(34):
                if (k21 * b) % 34 == 1:
                    k21_re = b
                    break
            if ii == 0:
                c1 += alf[((alf.find(i) - k12) * k11_re) % 34]
                ii += 1
                continue
            c1 += alf[((alf.find(i) - k22) * k21_re) % 34]
            k11, k21 = k21, k11 * k21
            k12, k22 = k22, k12 + k22
        else:
            c1 += i
    return c1


def main():
    message = input("Сообщение для зашифрования: ").upper()
    k11, k12 = [int(i) for i in input("Первая пара ключей k11 k12: ").split()]
    k21, k22 = [int(i) for i in input("Вторая пара ключей k21 k22: ").split()]
    print(affine(message, k11, k12, k21, k22))

    messaged = input("Сообщение для дешифрования: ").upper()
    k11, k12 = [int(i) for i in input("Первая пара ключей k11 k12: ").split()]
    k21, k22 = [int(i) for i in input("Вторая пара ключей k21 k22: ").split()]
    print(decode(messaged, k11, k12, k21, k22))


if __name__ == '__main__':
    main()
