def cezar(message, smeshenie):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!?.,() "
    itog = ''
    for i in message:
        mesto = alf.find(i)
        new_mesto = mesto + smeshenie
        if i in alf:
            itog += alf[new_mesto % 66]
        else:
            itog += i
    return itog


def main():
    message = input("Сообщение для зашифрования: ").upper()
    smeshenie = int(input("Ключ: "))
    print(cezar(message, smeshenie))

    messaged = input("Сообщение для дешифрования: ").upper()
    smeshenied = -int(input("Ключ: "))
    print(cezar(messaged, smeshenied))


if __name__ == '__main__':
    main()
