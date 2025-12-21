# Want to print out a square

def main():
    print_square(3);

def print_square(size):
    for i in range(size):
        # In here is a row. So now on every row, I want to print # 3 times
        print("#" * 5);
    print();

main();