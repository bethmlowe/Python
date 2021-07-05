#===============================================================================
#Program:       Average Sale Calculator
#Programmer:    Elizabeth Byrne
#Date:          June 19, 2021
#Abstract:      This program will input a salesperson's name follwed by the
#               first sale amount then the number of sales as indicated below
#               for a used car delearship. The program will then display the
#               sales person's average, highest, and lowest sale.
#===============================================================================

#define the main function
def main():

    #create a variable to control the loop
    keep_going = 'y'

    #create a counter for salespersons
    number_of_salespersons = 0

    #process each salesperson's sales
    while keep_going == 'y' or keep_going == 'Y':

        #use a function to process each salesperson
        process_salesperson()

        number_of_salespersons += 1

        #are there more salespersons?
        keep_going = input('Are there more salespersons? (enter y for yes): ')

    #display the total number of salespersons
    print ('There were', number_of_salespersons, 'salespersons processed.')

#process each salesperson's sales
def process_salesperson():

    #get the salesperson's name
    name = input("What is the salesperson's name? ")
    print ('Enter', name + "'s amount for first sale: "),
    first_sale = float(input())

    #validate the sale is > 0 and < 25000
    while first_sale < 0 or first_sale > 25000:
        print ("ERROR: the sale cannot be less than 0 or greater than 25000.")
        first_sale = float(input("Please enter a correct sale amount: "))

    #initialize total, lowest, and highest sale to first sale
    total_sales = first_sale
    lowest_sale = first_sale
    highest_sale = first_sale
    
    #get the number of sales for this salesperson
    print ('How many sales does', name, 'have?')
    number_of_sales = int(input())

    for number in range(2, number_of_sales + 1):

        #get the sales amount
        print ('Enter', name + "'s sale #" + str(number) + ':'),
        sale = float(input())

        #validate the sale is > 0 and < 25000
        while sale < 0 or sale > 25000:
            print ('ERROR: the sale cannot be less than 0 or grater than \
            25000.')
            sale = float(input("Please enter a correct sales amount: "))

        #accumulate the sales
        total_sales += sale

        #check for highest sale
        if sale > highest_sale:
            highest_sale = sale

        #check for lowest sale
        elif sale < lowest_sale:
            lowest_sale = sale

        #compute average sale
        average_sale = float(total_sales) / number_of_sales

        #display the average, highest, and lowest sale
        print('')
        print(name + "'s average sale was: $", format(average_sale, ".2f"), \
               sep='')
        print(name + "'s highest sale was: $", format(highest_sale, ".2f"), \
               sep='')
        print(name + "'s lowest sale was: $", format(lowest_sale, ".2f"), \
               sep='')
        print('')

#call the main function
main()
