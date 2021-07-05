#===============================================================================
#Program:       ATM Program
#Programmer:    Elizabeth Byrne
#Date:          6/2/21
#Abstract:      This program is a simulation of an ATM. It will process
#               deposits, withdrawls, and invalid transaction codes,
#               and provide a current balance.
#===============================================================================

#The main function definition
def main():
    Name = input("What is your name? ")
    Account_ID = input("What is your account ID? ")
    Transaction_Code = input("Press W or w for withdrawl, Press D or d for deposit ")
    Previous_Balance = float(input("What is your previous balance? "))
    Transaction_Amount = float(input("How much is the transaction amount? "))

    if Transaction_Code == "W" or Transaction_Code == "w":
        Withdrawl_Process(Previous_Balance, Transaction_Amount)
    elif Transaction_Code == "D" or Transaction_Code == "d":
        Deposit_Process(Previous_Balance, Transaction_Amount)
    else:
        Process_Invalid_Code(Previous_Balance)

#The Invalid Code Function Definition
def Process_Invalid_Code(Previous_Balance):
    New_Balance = Previous_Balance
    print ("Invalid Transaction Code: ")
    print ("Please type W or w for Withdrawl")
    print ("or D or d for Deposit")
    Print_Function(New_Balance)
    
#The Deposit Process Definition
def Deposit_Process(Previous_Balance, Transaction_Amount):
    New_Balance = Transaction_Amount + Previous_Balance
    Print_Function(New_Balance)

#The Withdrawl Process Definition
def Withdrawl_Process(Previous_Balance, Transaction_Amount):
    if Previous_Balance >= Transaction_Amount:
        New_Balance = Previous_Balance - Transaction_Amount
        Print_Function(New_Balance)
    else:
        print("Invalid Transaction: Not Sufficient Funds")
        New_Balance = Previous_Balance
        Print_Function(New_Balance)

#The Print Function Definition
def Print_Function(New_Balance):
    print ('Your balance is now $', format(New_Balance, '.2f'))

#Call the main function
main()
