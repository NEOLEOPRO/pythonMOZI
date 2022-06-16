def vig_encoder1(phrase, alph, key):
    """Зашифрование с помощью шифра Виженера с повторением кортокого лозунга"""
    ans = ''
    k = 0
    for i in phrase:
        ans += alph[(alph.find(i) + alph.find(key[k])) % len(alph)]
        k = (k + 1) % len(key)
    return ans


def vig_decoder1(phrase, alph, key):
    """Расшифрование с помощью шифра Виженера с повторением кортокого лозунга"""
    ans = ''
    k = 0
    for i in phrase:
        ans += alph[(alph.find(i) - alph.find(key[k])) % len(alph)]
        k = (k + 1) % len(key)
    return ans


def vig_encoder2(phrase, alph, key):
    """Зашифрование с помощью шифра Виженера с самоключом по открытому тексту"""
    ans = ''
    for i in phrase:
        ans += alph[(key + alph.find(i)) % len(alph)]
        key = alph.find(i)
    return ans


def vig_decoder2(phrase, alph, key):
    """Расшифрование с помощью шифра Виженера с самоключом по открытому тексту"""
    ans = ''
    for i in phrase:
        ans += alph[(alph.find(i) - key) % len(alph)]
        key = alph.find(alph[(alph.find(i) - key) % len(alph)])
    return ans


def vig_encoder3(phrase, alph, key):
    """Зашифрование с помощью шифра шифр Виженера с самоключом по шифртексту"""
    ans = ''
    for i in phrase:
        ans += alph[(alph.find(i) + key) % len(alph)]
        key = alph.find(alph[(alph.find(i) + key) % len(alph)])
    return ans


def vig_decoder3(phrase, alph, key):
    """Расшифрование с помощью шифра Виженера с самоключом по шифртексту"""
    ans = ''
    for i in phrase:
        ans += alph[(alph.find(i) - key) % len(alph)]
        key = alph.find(i)
    return ans


def main():
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!'.lower()
    print("Выберите вариацию шифра Виженера:")
    print("1 - шифр Виженера с повторением кортокого лозунга")
    print("2 - шифр Виженера с самоключом по открытому тексту")
    print("3 - шифр Виженера с самоключом по шифртексту")
    cipher = int(input())
    if cipher > 3 or cipher < 1:
        raise TypeError('Неправильный ввод')

    print("Выберите операцию:")
    print("1 - Зашифрование")
    print("2 - Расшифрование")
    type = int(input())
    if type < 1 or type > 2:
        raise TypeError('Неправильный ввод')

    print('Введите сообщение:')
    phrase = input()
    print('Введите ключ:')
    key = input()

    if cipher == 1:
        if type == 1:
            print('Шифр текст:', vig_encoder1(phrase, alph, key))
        else:
            print('Открытый текст:', vig_decoder1(phrase, alph, key))

    elif cipher == 2:
        if type == 1:
            print('Шифр текст:', vig_encoder2(phrase, alph, int(key)))
        else:
            print('Открытый текст:', vig_decoder2(phrase, alph, int(key)))

    elif cipher == 3:
        if type == 1:
            print('Шифр текст:', vig_encoder3(phrase, alph, int(key)))
        else:
            print('Открытый текст:', vig_decoder3(phrase, alph, int(key)))


if __name__ == '__main__':
    main()
