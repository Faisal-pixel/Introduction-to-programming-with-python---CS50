# Ask the user for a fraction that they input as X / Y.
# imediately int(isize) it lol. As in int(x)/int(y).
# do a try except block here since a value error can occur, and in the except block... pass it back so that it can reask the user
# also add an exception here because the bottom y can be 0 which could raise a ZaeroDivisionError, then pass back
# then we can go ahead and do a else...
# in the else, if nothing goes wrong we can do the division and multiply by 100%, round it to the nearest integer
# then if the percentage is 1% or less, return E, if it is 99% or greater, return F

def main():
    while True:
        try:
            user_input = input("Fraction: ") # expecting x/y
            # I then split
            x, y = user_input.split("/")
            divided_value = int(x)/int(y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            # If it goes well without an error...
            if divided_value > 1:
                pass
            elif divided_value < 0:
                pass
            else:
                break
    fuel_percentage = round(divided_value * 100)

    print("E" if fuel_percentage <= 1 else "F" if fuel_percentage >= 99 else f"{fuel_percentage}%")

main()
