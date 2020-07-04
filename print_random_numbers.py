import random
import argparse

parser = argparse.ArgumentParser(description='Script displays integers from 1 to 10 in random order')
args = parser.parse_args()


def main():
    numbers = list(range(1, 11))
    random.shuffle(numbers)
    for i in numbers:
        print(i)


if __name__ == '__main__':
    main()
