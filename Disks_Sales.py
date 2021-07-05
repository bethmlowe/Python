#===========================================================================
#Program: 		Disks
#Programmer: 	Elizabeth Byrne
#Date: 			  07/02/2021
#Abstract: 		This program reads data from an input file, formats a 
#				      printed report into columns.
#==============================================================================

#Create global constraints for the price of a CD and DVD
CW_RW_PRICE = 16.50
DVD_RW_PRICE = 21.75

def main():

	#initialize counters
	cd_customers_counter = 0
	dvd_customers_counter = 0
	total_payment_due = 0

	
	#create column headings line
	print('Customer Name \tCode\tSpindle\tPayment Due')
	print('')
	
	#create the try block of the exception handler
	try:
		#open file named disks.txt
		infile = open(r"C:\Users\Beth\Desktop\disks.txt", 'r')
		
		#read first line of the file which is the customer name field
		customer_name = infile.readline()
		
		#while a field is read continue processing
		while customer_name != '':
		
			#strip new line character from the customer name field and display
			customer_name = customer_name.rstrip('\n')
			print(customer_name, end='\t')
			
			#read code field. strip new line character and display
			code = infile.readline()
			code = code.rstrip('\n')
			print(code, end='\t')
			
			#read the spindles field. strip new line character and display
			spindles = infile.readline()
			spindles = int(spindles)
			print(format(spindles, '3.0f'), end='\t')
			
			#check code and compute payment due
			#increment appropriate counters
			if code == "c" or code == "C":
				payment_due = spindles * CW_RW_PRICE
				cd_customers_counter += 1
			elif code == "d" or code == "D":
				payment_due = spindles * DVD_RW_PRICE
				dvd_customers_counter += 1
			else:
				payment_due = 0
				
			#accumulate total payment due
			total_payment_due += payment_due
			
			#display invalid code or payment due
			if payment_due == 0:
				print('invalid code: no payment due')
			else:
				print('$', format(payment_due, '7,.2f'))
			
			#read the customer name field of the next record
			customer_name = infile.readline()
			
		#close input file
		infile.close()
		
		#display counters and total of payments due
		print('')
		print('Total customers that purchased CD-RWs: ', cd_customers_counter)
		print('Total customers that purchased DVD-RWs: ', dvd_customers_counter)
		print('')
		print('Total amounts of payments due: ', end='')
		print('$', format(total_payment_due, ',.2f'), sep='')
		
		#exception clause
		#display handler statement to gracefully respond
	except IOError:
		print('An error has occured trying to open or read disks.txt')
			
#call the main function
main()
