import afin, cryptomath
from PR3 import detectEnglish


def main():
    # myMessage = "KSNM)VHM()S(M)RSSC)QM)(MMZ)VS)NM,Z" #affine
    myMessage = "Y .QE(TQZE ZQEN  WEAQEZQQPE( E.QMP"  # cezar

    hackedMessage = hackAffine(myMessage)
    if hackedMessage == None:
        print('Failed to hack encryption.')


def hackAffine(message):
    for key in range(34 ** 2):
        keyA = key // 34
        if cryptomath.egcd(keyA, 34)[0] != 1:
            continue
        keyB = key % 34

        decryptedText = afin.decript(message, keyA, keyB)
        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print('Possible encryption hack:')
            print('Key pair A: {} B: {}'.format(keyA, keyB))
            print('Decrypted message:')
            print(decryptedText[:200])
            print()
            return decryptedText
    return None


if __name__ == '__main__':
    main()
