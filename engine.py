import sys


def error(msg):
    print("ERROR: ",msg)
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        error("Too few args")

    print(sys.argv[1:])
