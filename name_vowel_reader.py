"""
Asks user to input a name and checks the number of vowels and letters in the name.
"""


def main():
    name = input("Name: ")
    number_vowels = count_vowels(name)
    number_letters = count_letters(name)
    print("Out of {} letters, {}\nhas {} vowels".format(number_letters, name, number_vowels))


def count_vowels(string):
    number_of_vowels = 0
    vowels = "AaEeIiOoUu"
    for char in string:
        if char in vowels:
            number_of_vowels = number_of_vowels + 1
    return number_of_vowels


def count_letters(string):
    number_of_letters = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for char in string:
        if char in letters:
            number_of_letters = number_of_letters + 1
    return number_of_letters


main()
