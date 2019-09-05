from models import *

Borrower = User('Borrower', 'lotfy', 0)
Investor =	User('Investor', 'Amr', 20000)

Loan_Request = LoanRequest(Borrower.get_UserName(), 5000, 6)
Offer = Offer(Loan_Request.ID, Investor.get_UserName(), 5000, 6, 15)

try:
	Borrower.add_Loan_Request(Loan_Request)
	print ('Loan Request with below details was submitted Succefully\n')
	print(Loan_Request)
except Exception as err:
	print (err)

try: 
	Investor.add_Offer(Offer)
	print ('Loan Offer with below details was submitted Succefully\n')
	print(Offer)
except Exception as err:
	print (err)

print ('Loan with below details was added to the system:\n')
Loan = Loan(Loan_Request,Offer,'Funded')
print(Loan)
