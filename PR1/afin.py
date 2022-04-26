def affine(p: str, k1: int, k2: int):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !?.,():"
    c = ""
    alfz = ""
    if gcd(k1) != 1:
        print("Warn: k1 не взаимно простое с 34, дешифрование с данным ключём не получится")
    for i in alf:
        alfz += alf[(alf.find(i) * k1 + k2) % 34]
    for i in p:
        if i in alf:
            c += alfz[alf.find(i)]
        else:
            c += i
    return c


def gcd(x: int, y=34):
    s = 0
    if x > y:
        temp = y
    else:
        temp = x
    for i in range(1, temp + 1):
        if (x % i == 0) and (y % i == 0):
            s = i
    return s


def decript(p: str, k1: int, k2: int):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !?.,():"
    c1 = ""
    alfz = ""
    k1_re = 0
    if gcd(k1) != 1:
        return "Error: k1 не взаимно простое с 34"
    for i in range(34):
        if (k1 * i) % 34 == 1:
            k1_re = i
            break
    for i in alf:
        alfz += alf[((alf.find(i) - k2) * k1_re) % 34]
    for i in p:
        if i in alf:
            c1 += alfz[alf.find(i)]
        else:
            c1 += i
    return c1


def main():
    message = input("Сообщение для зашифрования: ").upper()
    k1 = int(input("Первый ключ: "))
    k2 = int(input("Второй ключ: "))
    print(affine(message, k1, k2))

    messaged = input("Сообщение для дешифрования: ").upper()
    k1 = int(input("Первый ключ: "))
    k2 = int(input("Второй ключ: "))
    print(decript(messaged, k1, k2))


if __name__ == '__main__':
    main()
