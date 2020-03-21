import time


def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total


# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
print(total_length(["", '', "", '']))

words = ["echidna", "dingo", "crocodile", "bunyip"]
words.append("platypus")

# def password_check():
#     while input("Password: ") != "swordfish":
#         print("Wrong! Try again!")
#     print("Okey, come on it!")


# password_check()

n = 0
while n < 3:
    print(n)
    n += 1

n = 1
while n <= 3:
    print(n)
    n += 1

n = 10
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("Blastoff!")

s = "Tenochtitan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])

s = "abracadabra"
index = len(s)
while index > 0:
    print(s[:index])
    index -= 1


# 2 examples of loops - for and while which does the same thing
word = "cat"
for index in range(len(word)):
    print(index)


index = 0
word = "cat"
while index < len(word):
    print(index)
    index += 1


# 2 examples of loops - for and while which does the same thing
word = "cat"
for index in range(len(word)):
    print(word[index])


index = 0
word = "cat"
while index < len(word):
    print(word[index])
    index += 1

# 2 examples of functions - with for and while loop which does the same thing


def count_character(string, target):
    total = 0
    for ch in string:
        if ch == target:
            total += 1
    return total


print(count_character("bonobo", "o"))


def count_caracter(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total


print(count_character("bonobo", "o"))

index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])

index = 0
sentence = "Hi friend. How are you?"
while index < len(sentence) and sentence[index] != ".":
    index += 1
print(sentence[:index])

# Linear search while loop used


def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        index += 1
    return s[:index]


print(until_dot("Great. Done"))

# Linear search for loop used


def until_dott(s):
    for index in range(len(s)):
        if s[index] == '.':
            return s[:index]
    return s


print(until_dott("Well done. Thank you"))

# Exit from the infinite loop by using break statement
# def no_repeating():
#     words = []
#     while True:
#         word = input("Tell me a word: ")
#         if word in words:
#             print("You told me that word already!")
#             break
#         words.append(word)
#     return words


def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index: index + len(substring)] == substring:
            return True
        index += 1
    return False


# This one should return False
print(is_substring('bad', 'abracadabra'))

# This one should return True
print(is_substring('dab', 'abracadabra'))
