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


def password_check():
    while input("Password: ") != "swordfish":
        print("Wrong! Try again!")
    print("Okey, come on it!")


password_check()
