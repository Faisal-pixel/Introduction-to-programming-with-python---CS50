import random


def main():
    level = get_level()
    current_question_no = 1
    total_score = 0
    while current_question_no <= 10:
        x = generate_integer(level)
        y = generate_integer(level)

        solution = x + y
        trials = 0
        while trials < 3:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer != solution:
                    raise ValueError()
            except ValueError:
                print("EEE")
                pass
            else:
                break
            trials += 1
        if trials == 3:
            print(f"{x} + {y} = ", solution)
        else:
            total_score += 1

        current_question_no += 1

    print("Score:", total_score)


def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
        except ValueError:
            pass
        else:
            if user_input not in (1, 2, 3):
                pass
            else:
                return user_input

def generate_integer(level):
    if level not in (1, 2, 3):
        raise ValueError()
    # The math below is for range of n digits, it is 10^(n-1) to 10^n - 1 except for when n is 1, then the start point is 0
    return random.randint(0 if level == 1 else pow(10, level - 1), pow(10, level) - 1)


if __name__ == "__main__":
    main()
