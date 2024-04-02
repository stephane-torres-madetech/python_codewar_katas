""" Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that! """



def remove_every_other(array: list):
    for index in range(len(array)):
        print(index)
        if index % 2 != 0:
            array.pop(index)

    return array