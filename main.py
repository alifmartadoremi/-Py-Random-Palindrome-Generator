__author__ = "kvda-creator"

import string
import random

class mainClass():
    def mainFunc(self):
        offset = 1
        print("---")
        print("Generate Random Palindrome")
        print("---")
        Palengthdrome = input("Masukkan panjang kata palindrome : ")
        print("---")
        print(" ")
        while(offset==1):
            palindrome = ''.join(random.choice(string.ascii_lowercase) for _ in range(int(Palengthdrome)))
            if palindrome == palindrome[::-1]:
                print(palindrome," dengan ",palindrome[::-1]," sama.")
                break
            else:
                continue
        print("---")
        print("copyright 2021 kvda-creator")

if __name__ == '__main__':
    mainClass().mainFunc()