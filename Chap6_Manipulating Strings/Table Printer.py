tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

colWidths = []

for list in tableData:
    for data in list:
        colWidths.append(len(data))

longest = max(colWidths)


def printTable(tableData):
    for data in range(4):
        for list in range(3):
            print(tableData[list][data].rjust(longest), end=" ")
        print(" ")


printTable(tableData)
