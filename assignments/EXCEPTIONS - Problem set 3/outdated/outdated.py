def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        user_input = input("Date: ")
        try:
            if "/" in user_input:
                month, day, year = user_input.split("/")
                month = int(month)
            elif "," in user_input:
                month, day, year = user_input.split()
                day = day.replace(",", "")
                month = months.index(month) + 1
            else:
                raise ValueError


            day = int(day)
            year = int(year)
            if day > 31:
                raise ValueError("Day is greater than 30 days")
            if month > 12:
                raise ValueError("Month is greater than 12 months")
            break
        except ValueError: # I get value error here because when I use the index to check whether / or , exist in the string and its not there, then python raises a value error
            pass

    print(f"{year}-{month:02}-{day:02}")


main()
