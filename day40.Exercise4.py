import random
import string


def coding(word):

    if len(word) < 3:
        word = word[::-1]
        return word

    else:
        first_letter = word[: len(word) - (len(word) - 1)]
        word = word[1:] + first_letter
        for i in range(3):
            random_letter = random.choice(string.ascii_letters)
            word = word + random_letter
            random_letter = random.choice(string.ascii_letters)
            word = random_letter + word
        return word


def decoding(word):
    if len(word) < 3:
        word = word[::-1]
        return word
    else:
        word = word[3:-3]
        last_letter = word[-1:]
        word = last_letter + word[:-1]
        return word


x = int(input("Select one Option : \n1. Code\n2. Decode\n"))
while x > 2 or x < 1:
    print("Only Select 1 or 2 Option")
    x = int(input("Select agin : \n1. Code\n2. Decode\n"))


if x == 1:
    word = input("Enter the String you want to code : ")

    word = word.split(" ")
    str = ""
    for w in word:
        w = coding(w)
        str += w + " "

    print("Your Coded String Is : ", str)

    # # b = word
    # coded_word = ""
    # while True:
    #     j = word.find(" ")
    #     if j == -1:
    #         coded_word = coded_word + coding(word)
    #         break
    #     word_part = word[:j]
    #     coded_word = coded_word + coding(word_part) + " "
    #     word = word[j + 1 :]

    # print("Your Coded String Is : ", coded_word)

else:
    word = input("Enter the String you want to decode : ")
    word = word.split()
    str = ""
    for w in word:
        w = decoding(w)
        str += w + " "
    print("Your DeCoded String Is : ", str)

    # # b = word
    # decoded_word = ""
    # while True:
    #     j = word.find(" ")
    #     if j == -1:
    #         decoded_word = decoded_word + decoding(word)
    #         break
    #     word_part = word[:j]
    #     decoded_word = decoded_word + decoding(word_part) + " "
    #     word = word[j + 1 :]

    # print("Your DeCoded String Is : ", decoded_word)
