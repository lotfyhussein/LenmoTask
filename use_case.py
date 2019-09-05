from models import *
import time

Borrower = User('Borrower', 'Lotfy', 0)
Investor =	User('Investor', 'Ahmed', 20000)

Loan_Request = LoanRequest(Borrower.Get_UserName(), 5000, 6)
Offer = Offer(Loan_Request.ID, Investor.Get_UserName(), 5000, 6, 15)

try:
	Borrower.Add_Loan_Request(Loan_Request)
	print ('Loan Request with below details was submitted Succefully\n')
	print(Loan_Request)
	print('---------------')
except Exception as err:
	print (err)
time.sleep(3)
try: 
	Investor.Add_Offer(Offer)
	print ('Loan Offer with below details was submitted Succefully\n')
	print(Offer)
	print('---------------')
except Exception as err:
	print (err)
time.sleep(3)   
print ('Loan with below details was added to the system:\n')
Loan = Loan(Loan_Request,Offer,'Funded')
print(Loan)
print('---------------')
time.sleep(3)   


Loan_Payments = Loan.Schedule_Loan_Payments()

for i in range (len(Loan_Payments)):
	time.sleep(3)
	print('Payment with below details was paid:\n')   
	print (Loan_Payments[i])
	print('---------------')
