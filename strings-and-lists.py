print("Hello world!")

print("That's Python")

print('I said, "It\'s cool')


print('"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.\n"It\'s long," said the Knight,"but it\'s very, very beautiful."')

print("""
"Is it very long?" Alice asked, for she had heard a good deal of poetry that day."
"It's long," said the Knight,"but it\'s very, very beautiful."
""")


def too_long(s):
    length = len(s)
    if length > 140:
        return True
    else:
        return False


print(too_long("I'm a short string!"))
print(too_long("For score and seven years ago our fathers bought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.!"))

for ch in "hello world!":
    print(ch)


for ch in "Hello!":
    print(ch)
    if ch == "!":
        print("I am excited too!!!")

for ch in "bonobos":
    if ch == "o":
        print("hi")

count = 0
for ch in "bonobos":
    if ch == "o":
        count = count + 1

print(count)


def count_character(string, target):
    count = 0

    for ch in "bonobos":
        if ch == "o":
            count = count + 1
    return count


print(count_character("oxen and foxen all live in boxen", "x"))
print(count_character("that letter isn't here", "x"))
print(count_character("the goofy doom of the balloon goons", "o"))


def start_K(word):
    if word[0] == "K":
        return True
    else:
        return False


print(start_K("Kelly"))
print(start_K("Abe"))
