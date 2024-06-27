from getpass import getpass

print("---------------------------------------")
print("|---------Welcome to ABC Bank---------|")
print("---------------------------------------")

pswd = 1102
pin = int(getpass("Enter your 4 digit pin:"))
bal = int(220000)

while True:
 if pin == pswd:
      print("The default money in your account is:",bal)
      print(1,"1.Balance Inquiry")
      print(2,"2.Withdraw Amount")
      print(3,"3.Deposit Amount")
      print(4,"4.Exit")

      option = int(input(""))
      if  option == 1 :
            print("Your balance is:",bal)

      if option == 2 :
            wamot = int(input("Enter amount you want to withdraw:"))
            rembal = bal - wamot
            if wamot<=bal:
               print("You have withdrawed :", wamot)
               print("Your remaining balance is :", rembal)
            elif wamot >=bal:
               print("Invalid Amount") 

      if option == 3 :
            addamot = int (input("Enter your amount to be added:"))
            addbal = bal + addamot
            print("Your updated balance is :",addbal)  

      if option == 4 :
            print("Thank you for using our bank.")
            break
 else:
      print("Your pin is invalid.") 
      break                 
      
    
 
