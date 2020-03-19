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
