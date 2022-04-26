import detectEnglish, cryptomath, afinrecur


def main():
    myMessage = "X.:(FL?.:ZJHPH(HFQ:F?BSWBMQGBSUNKK"

    hackedMessage = hackAffine(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')


def hackAffine(message):
    for key1 in range(34 ** 2):
        for key2 in range(34 ** 2):
            keyA1 = key1 // 34
            keyA2 = key2 // 34
            keyB1 = key1 % 34
            keyB2 = key2 % 34
            if cryptomath.egcd(keyA1, 34)[0] == 1 and cryptomath.egcd(keyA2, 34)[0] == 1 and \
                    cryptomath.egcd(keyA1, keyA2)[0] == 1:
                decryptedText = afinrecur.decript(message, keyA1, keyA2, keyB1, keyB2)
                if detectEnglish.isEnglish(decryptedText):
                    print('Possible encryption hack:')
                    print('Key pair A1: {} A2: {} B1: {} B2: {}'.format(keyA1, keyA2, keyB1, keyB2))
                    print('Decrypted message:')
                    print(decryptedText[:200])
                    print()
                    print('Enter D for done, or just press Enter to continue hacking:')
                    response = input('> ')

                    if response.strip().upper().startswith('D'):
                        return decryptedText

    return None


if __name__ == '__main__':
    main()
