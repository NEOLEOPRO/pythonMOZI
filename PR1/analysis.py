import argparse
from collections import OrderedDict
from curses.ascii import ispunct


def sort_dict_by_value_reverse(indict):
    outdict = OrderedDict()

    indictsorted = sorted(indict, key=indict.__getitem__, reverse=True)

    for i in indictsorted:
        outdict[i] = indict[i]

    return outdict


def build_ngram_counts(inputtext=None, n=1, countspace=False, countpunctuation=False):
    if inputtext is None or n < 1:
        return None

    ngrams = dict()
    for c in range(len(inputtext)):
        if not (inputtext[c].isalpha() or
                (ispunct(inputtext[c]) and countpunctuation is True and inputtext[c] != '\n') or
                (inputtext[c] == ' ' and countspace is True)):
            continue

        i = 0
        ngram = ""
        while len(ngram) < n and c+i < len(inputtext):
            if (inputtext[c+i].isalpha() or
                (ispunct(inputtext[c+i]) and countpunctuation is True and inputtext[c+i] != '\n') or
                    (inputtext[c+i] == ' ' and countspace is True)):
                ngram += inputtext[c+i]
            i += 1

        if len(ngram) == n:
            if ngram in ngrams:
                ngrams[ngram] += 1
            else:
                ngrams[ngram] = 1

    return sort_dict_by_value_reverse(ngrams)


def main():
    ciphertext = "Y .QE(TQZE ZQEN  WEAQEZQQPE( E.QMP"

    cipherlettercounts = build_ngram_counts(ciphertext, 1)

    print("Letter Frequency:")
    for c in cipherlettercounts:
        print("{0} = {1}".format(c, cipherlettercounts[c]/len(ciphertext)))
    print("")


if __name__ == '__main__':
    main()