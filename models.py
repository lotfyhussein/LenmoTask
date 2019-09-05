import uuid
class User:
    def __init__(self, type, username, balance):
        self.type = type
        self.username = username
       	self.balance = balance
        self.LoanRequests = []
        self.Offers = []

    def add_Loan_Request(self, LoanRequest):
    	if self.type == 'Borrower':
    		self.LoanRequests.append(LoanRequest)
    	else:
    		raise Exception('an Investor Cannot perform this request')
    def add_Offer(self, Offer):
    	if self.type == 'Investor':
    		if self.balance >= Offer.amount + Offer.Lenmo_Fees:
    			self.Offers.append(Offer)
    		else:   
    			raise Exception('Insufficient Funds')
    	else:
    		raise Exception('a Borrower Cannot perform this request')


    def get_User_Type(self):
    	return self.type

    def get_UserName(self):
   		return str(self.username)

    def get_User_Loans(self):
    	if self.type == 'Borrower':
    		return self.LoanRequests
    	else:
    		return self.Offers

class LoanRequest:
    def __init__(self, Borrower, amount, period):
        self.ID = uuid.uuid4()
        self.Borrower = Borrower	
        self.amount = amount
        self.period = period	
    def getAmount(self):
    	return self.amount
    def getPeriod(self):
    	return self.period
    def __str__(self):
    	return "Loan_Request_ID: {},\nBorrower: {},\namount: {},\nperiod: {}\n".format(self.ID, self.Borrower, self.amount,self.period)



class Offer:
    def __init__(self, Loan_Request_ID, Investor, amount, period, interest):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request_ID
        self.Investor = Investor	
        self.amount = amount
        self.period = period		
        self.interest = interest
        self.Lenmo_Fees = 3
    def get_Amount(self):
    	return self.amount
    def get_Period(self):
    	return self.period
    def get_Interest(self):
    	return self.interest
    def get_Investor(self):
    	return self.Investor
    def __str__(self):
    	return"Offer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\namount: {},\nperiod: {},\nInterest: {}\n".format(self.ID, self.Loan_Request_ID, self.Investor, self.amount,self.period, self.interest)




# class Loan:
#     def __init__(self,Investor, amount, period, interest, Borrower, status):
#     def get_Status(self):
#     	return self.status
#     def print_Details(self):
#     	print("Investor: {}, Borrower: {} , amount: {}, period: {}, Interest: {}, Status: {}".format(self.Investor, self.Borrower, self.amount,self.period, self.interest, self.status))


class Loan:
    def __init__(self,Loan_Request, Offer, status):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request.ID
        self.Offer_ID = Offer.ID
        self.Investor = Offer.Investor	
        self.amount = Offer.amount
        self.period = Offer.period		
        self.interest = Offer.interest
        self.status = status
    def get_Status(self):
    	return self.status
    def __str__(self):
    	return"Offer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\namount: {},\nperiod: {},\nInterest: {},\nStatus: {}\n".format(self.ID, self.Loan_Request_ID, self.Investor, self.amount,self.period, self.interest, self.status)






