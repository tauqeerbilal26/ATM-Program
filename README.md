# ABC Bank ATM Program

This is a simple ATM simulation program for ABC Bank. It allows users to check their balance, withdraw money, deposit money, and exit the program.

## How to Use

1. Run the program.
2. Enter your 4-digit PIN when prompted.
3. Choose from the available options:
   - Balance Inquiry
   - Withdraw Amount
   - Deposit Amount
   - Exit

## Program Details

- The default PIN is `1102`.
- The initial balance is set to `220,000`.

## Features

- **Balance Inquiry:** Displays the current balance in the account.
- **Withdraw Amount:** Allows the user to withdraw a specified amount of money, provided there are sufficient funds.
- **Deposit Amount:** Allows the user to deposit a specified amount of money into the account.
- **Exit:** Exits the program.

## Code

```python
from getpass import getpass

print("---------------------------------------")
print("|---------Welcome to ABC Bank---------|")
print("---------------------------------------")

pswd = 1102
pin = int(getpass("Enter your 4 digit pin:"))
bal = int(220000)

while True:
 if pin == pswd:
      print("The default money in your account is:", bal)
      print(1, "1.Balance Inquiry")
      print(2, "2.Withdraw Amount")
      print(3, "3.Deposit Amount")
      print(4, "4.Exit")

      option = int(input(""))
      if option == 1:
            print("Your balance is:", bal)

      if option == 2:
            wamot = int(input("Enter amount you want to withdraw:"))
            if wamot <= bal:
               bal -= wamot
               print("You have withdrawn:", wamot)
               print("Your remaining balance is:", bal)
            else:
               print("Invalid Amount") 

      if option == 3:
            addamot = int(input("Enter your amount to be added:"))
            bal += addamot
            print("Your updated balance is:", bal)  

      if option == 4:
            print("Thank you for using our bank.")
            break
 else:
      print("Your pin is invalid.") 
      break 
