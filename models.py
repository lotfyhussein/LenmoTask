class User:
    def __init__(self, type, username, balance):
        self.type = type
        self.username = username
       	self.balance = balance
        self.LoanRequests = []
        self.Offers = []

    def addLoanRequest(self, LoanRequest):
    	if self.type == 'Borrower':
    		self.LoanRequests.append(LoanRequest)
    		return True
    	else:
    		print ('Please Log in as an Borrower to perform this request')
    		return False

    def addOffer(self, Offer):
    	if self.type == 'Investor':
    		if self.balance >= Offer.amount + 3:
    			self.Offers.append(Offer)
    			return True
    		else:
    			print ('Insufficient Funds')   
    			return False 		    			
    	else:
    		print ('Please Log in as an Investor to perform this request')    	
    		return False	

    def getUserType(self):
    	return self.type

    def getUserName(self):
   		return str(self.username)

    def getUserLoans(self):
    	if self.type == 'Borrower':
    		return self.LoanRequests
    	else:
    		return self.Offers

class LoanRequest:
    def __init__(self, Borrower, amount, period):
        self.Borrower = Borrower	
        self.amount = amount
        self.period = period	
    def getAmount(self):
    	return self.amount
    def getPeriod(self):
    	return self.period
    def printDetails(self):
    	print("Borrower: {}, amount: {}, period: {}".format(self.Borrower, self.amount,self.period))



class Offer:
    def __init__(self, Investor, amount, period, interest):
        self.Investor = Investor	
        self.amount = amount
        self.period = period		
        self.interest = interest
    def getAmount(self):
    	return self.amount
    def getPeriod(self):
    	return self.period
    def getInterest(self):
    	return self.interest
    def getInvestor(self):
    	return self.Investor
    def printDetails(self):
    	print("Investor: {}, amount: {}, period: {}, Interest: {}".format(self.Investor, self.amount,self.period, self.interest))




class Loan(Offer):
    def __init__(self,Investor, amount, period, interest, Borrower, status):
        super().__init__(Investor, amount, period, interest)
        self.Borrower = Borrower
        self.status = status
    def getStatus(self):
    	return self.status
    def printDetails(self):
    	print("Investor: {}, Borrower: {} , amount: {}, period: {}, Interest: {}, Status: {}".format(self.Investor, self.Borrower, self.amount,self.period, self.interest, self.status))



