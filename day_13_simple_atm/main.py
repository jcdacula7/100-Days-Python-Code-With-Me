#   SIMPLE ATM SIMULATION
#   LIMITATIONS: not user proof, very simple


#   default account amount
account = 100.00


#   header formatting, welcome!
space = 60
print()
print("$" * space)
print()
print("Welcome to Simple ATM".center(space))
print()
print("$" * space)


while True:
    #   show menu
    print("""
                    1 : Deposit
                    2 : Withdraw
                    3 : Show Balance
        """)

    #   get user choice
    choice = int(input("What do you want to do?:  "))

    #   check choice
    if choice == 1:
        #   deposit
        deposit = float(input("How much do you want to deposit?: "))
        account += deposit
        print(f"\nYou deposited $ {deposit:,.2f} into your account")
        print(f"Your new balance: $ {account:,.2f}")
    elif choice == 2:
        #   withdraw
        withdraw = float(input("How much do you want to withdraw?: "))
        if account >= withdraw:
            account -= withdraw
            print(f"\nYou withdraw $ {withdraw:,.2f} from your account")
            print(f"Your new balance: $ {account:,.2f}")
        else:
            print("\nYou don't have enough money")
            print(f"Current balance: $ {account:,.2f}")
    elif choice == 3:
        print(f"Current Balance: $ {account:,.2f}")
    else:
        print("That's not a valid choice")

    #   check if want to make another transaction
    another_transaction = input(
        "\nDo you want to make another transaction? [Y/N]: "
    ).lower()

    #   end loop if N or n
    if another_transaction == "n":
        break


print("\nThank you for using the Simple ATM")
