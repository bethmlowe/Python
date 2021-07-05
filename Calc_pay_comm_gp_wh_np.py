#===============================================================================
# Program:      Homework 3
# Programmer:   Elizabeth Byrne-Lowe
# Date:         May 29, 2021
# Abstract:     This program uses functions to calculate pay, commission,
#               gross pay, withholding, and net pay.
#
#===============================================================================

def main():
    display_message()

    #Get name
    employee_name=input("Enter employee's name: ")

    #Get Sales
    sales_amount = float(input("Enter the sales amount: "))

    #Get Hours
    hours_worked = int(input("Enter hours worked by this employee: "))

    #Calculate Hourly Pay
    hourly_pay = hours_worked * hourly_pay_rate

    #Calculate Commission
    commission = sales_amount * commission_rate

    #Calculate Gross Pay
    gross_pay = hourly_pay + commission

    #Calculate Withholding
    withholding = gross_pay * withholding_rate

    #Calculate Net Pay
    net_pay = gross_pay - withholding
    display_results(hourly_pay, commission, gross_pay, withholding, net_pay)

def display_message():
        print ("This program calculates the salesperson's pay.")
        print ("Five values are displayed:")
        print ( "hourly pay, commission, gross pay, withholding, and net pay.")
        print ("")

def display_results(hourly_pay, commission, gross_pay, withholding, net_pay):
        print ("The hourly pay amount is: %.2f" % hourly_pay)
        print ("The commission amount is: %.2f" % commission)
        print ("The gross pay amount is: %.2f" % gross_pay)
        print ("The withholding amount is: %.2f" % withholding)
        print ("The net pay amount is: %.2f" % net_pay)

# define global constants and call main
hourly_pay_rate = float(7.50)
commission_rate = float(0.05)
withholding_rate = float(0.25)
main ()
