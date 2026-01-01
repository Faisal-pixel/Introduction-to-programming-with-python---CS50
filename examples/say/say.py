import cowsay
import sys

def main():
    if len(sys.argv) == 2:
        cowsay.cow("Hello, " +sys.argv[1])


main()