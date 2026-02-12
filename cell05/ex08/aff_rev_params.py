import sys

args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    for word in reversed(args):
        print(word)