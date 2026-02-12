import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    count = 0

    for char in text:
        if char == "z":
            count += 1

    if count == 0:
        print("none")
    else:
        print("z" * count)
