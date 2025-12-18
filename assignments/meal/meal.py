"""
Docstring for assignments.meal.meal

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

"""

def main():
    user_input = input("What time is it? ");
    converted_time = convert(user_input);

    if 7 <= converted_time <= 8:
        print("breakfast time");
    elif 12 <= converted_time <= 13:
        print("lunch time");
    elif 18 <= converted_time <= 19:
        print("dinner time");

def convert(time):
    # This function will conver the time from 7:30 to 7.5, how do i go about it?
    # We know the two parts of a time shows hour and minutes, the first part on the 24 hour scale shows the number of hours from 00:00 or 12am
    # Whule the second part which is the minutes is basically minute lol, what I mean is the minutes into the next hour. So in a way they are kind
    # of independent on each other and we can seperate them, convert the minute (left side) to hours and add it to the right part to know the total
    # number of hours from 12am.
    hour, minute = time.split(":");
    # 60 mins = 1hr, then x mins = x/60 hr
    total_hours = round(float(hour) + (float(minute)/60), 2);
    return total_hours;


if __name__ == "__main__":
    main()
