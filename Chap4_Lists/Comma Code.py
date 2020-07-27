# Comma Code

spam = ["apples", "bananas", "tofu", "cats"]

list = spam


def enumerate(listName):
    for a in range(len(list) - 1):
        print(list[a] + ", ", end="")
    print("and ", end="")
    print(list[-1])


enumerate(list)

