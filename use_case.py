from models import *
import time
#######################################################
# Adding a Borrower and an Investor To The System
Borrower = User('Borrower', 'Lotfy', 0)
Investor =	User('Investor', 'Ahmed', 20000)
#######################################################
# Intiating A Loan Request & an Offer for that Request
Loan_Request = LoanRequest(Borrower.Get_UserName(), 5000, 6) 
Offer = Offer(Loan_Request.ID, Investor.Get_UserName(), 5000, 6, 15)
#######################################################
# Adding the Request to the Borrower's list of requests
try:
	Borrower.Add_Loan_Request(Loan_Request)
	print ('Loan Request with below details was submitted Succefully\n')
	print(Loan_Request)
	print('---------------')
except Exception as err:
	print (err)
time.sleep(3) #We wait 3 seconds to simulate the scenario
#######################################################
# Adding the Offer to the Investor's list of requests
try: 
	Investor.Add_Offer(Offer)
	print ('Loan Offer with below details was submitted Succefully\n')
	print(Offer)
	print('---------------')
except Exception as err:
	print (err)
time.sleep(3)   
############################################################################
# Assuming the Borrower has accepted the offer, we add the off to the system
Loan = Loan(Loan_Request,Offer)
print ('Loan with below details was added to the system:\n')
print(Loan)
print('---------------')
time.sleep(3)   
#######################################################
# Now the Loan Payments are scheduled, and all of them has a status of 'Due'
Loan_Payments = Loan.Get_Loan_Payments()
print('All Scheduled Payments:\n')
for i in range (len(Loan_Payments)):
	print('Payment :{}\n'.format(i+1))   
	print (Loan_Payments[i])
	print('---------------')
############################################
# Now the Borrower will pay all payments, one at a time each month, and their status will change to 'Paid'
for i in range (len(Loan_Payments)):
	time.sleep(3)
	Loan_Payments[i].Update_Status('Paid') 
	print('Payment {} was paid:\n'.format(i+1))   
	print (Loan_Payments[i])
	print('---------------')
Loan.Update_Status()
####################################################
# Now Status of the Loan Should be 'Completed'
print ('Current Status of the Loan\n')
print (Loan)
