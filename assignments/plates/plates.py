def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # This function checks if the input is valid
    #1. All plates must start with at least two letters. (so confirm that the first two are letters by first slicing the string and then using .isalpha
    # to confirm that they are letters. I cant)
    # 2. The length of a vanity plate must contain at most 6 characters and at least 2 characters
    # 3. Numbers cannot be used in the middle of a plate.
    # 4. No periods, spaces or punctuation marks. So I will use .isalnum which returns true if all characters are either numbers or characters

    # 1st: No periods, spaces or punctuation marks. So I will use .isalnum which returns true if all characters are either numbers or characters
    # 2nd: The length of a vanity plate must contain at most 6 characters and at least 2 characters
    # 3rd: All plates must start with at least two letters. (so confirm that the first two are letters by first slicing the string and then using .isalpha
    # to confirm that they are letters. I cant)
    # 4th: Numbers cannot be used in the middle of a plate.

    if no_periods_spaces_pmarks(s) and lenght_is_valid(s) and s_starts_with_two_letters(s) and no_numbers_in_middle(s):
        return True
    else:
        return False


def no_periods_spaces_pmarks(s):
    return s.isalnum()

def lenght_is_valid(s):
    return 2 <= len(s) <= 6

def s_starts_with_two_letters(s):
    return s[:2].isalpha()

def no_numbers_in_middle(s):
    if s.isalpha():
        return True
    where_numbers_start = "";
    for index, char in enumerate(s):
        if char.isdigit():
            where_numbers_start += s[index:]
            break
    if where_numbers_start[-1:].isalpha(): # if the last digit is a letter then return false
        return False
    else:
        # only select a character and join into the string if it is a number
        return True if where_numbers_start.isdigit() and where_numbers_start[:1] != "0" else False

main()
