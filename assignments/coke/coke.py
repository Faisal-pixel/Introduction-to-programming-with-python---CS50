# TODO
# 1. Create a variable change_owed = 50
# 2. Then While amount_due is > 0:
# 3. Will print to the user "Amount Due: change_owed"
# 4. I will input Insert coin:
# 5. match inserted_coin:
# 6. case 25: then amount_due - 25
# 7. case 10: then amount_due - 10
# 8. case 5: then amount_due - 5
# 9. case _ ; then amount_due - 0;

def main():
    amount_due = 50
    change_owed = 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        inserted_coin = int(input("Insert Coin: "))
        match inserted_coin:
            case 25:
                # if inserted_coin > amount_due then set change_owed to inserted_coin - amount_due
                change_owed = (inserted_coin - amount_due) if inserted_coin > amount_due else 0
                amount_due = amount_due - 25 if amount_due > 25 else 0
            case 10:
                change_owed = (inserted_coin - amount_due) if inserted_coin > amount_due else 0
                amount_due = amount_due - 10 if amount_due > 10 else 0
            case 5:
                change_owed = (inserted_coin - amount_due) if inserted_coin > amount_due else 0
                amount_due = amount_due - 5 if amount_due > 5 else 0
            case _:
                amount_due = 50
    print(f"Change Owed: {change_owed}");

main()
