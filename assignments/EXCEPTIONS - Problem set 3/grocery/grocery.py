def main():
    grocery_list = {} # {"grocery_item": number of times inputed}
    while True:
        try:
            user_input = input("").upper();
            if user_input in grocery_list:
                grocery_list[user_input] += 1 # if the inputed item already exists in the grocery_list, then we want to in crease the count
            else:
                grocery_list[user_input] = 1
        except EOFError:
            print("")
            break
    sorted_groceries = sorted(grocery_list)
    print(*[f"{grocery_list[item]} {item}" for item in sorted_groceries], sep="\n") # the meaning of * is it unpacks an iterable. Check explanation here: https://chatgpt.com/g/g-p-69283b7352048191bd487312008c1cca-cs50/c/6951139f-44ac-832c-882a-4add722a5589
main()

# Can also do it this way: 

def main():
    grocery_list = {}
    while True:
        try:
            user_input = input("").upper();
        except EOFError:
            print("")
            break
        grocery_list = grocery_list.get(user_input, 0) + 1 # so basically i want to get a user_input from the grocery_list dictionary but return a 0 if it doesnt exist there, then add 1
    sorted_groceries = sorted(grocery_list)
    print(*map(grocery_list.get, sorted_groceries), sep="\n") # the map function takes ina. function that is applied to every member of an iterable, in our case a dictionary... then second member is the list that contains the values we want to pass into the function.
main()