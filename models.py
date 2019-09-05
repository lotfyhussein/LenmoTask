import uuid
class User:
    def __init__(self, Type, Username, Balance):
        self.Type = Type
        self.Username = Username
       	self.Balance = Balance
        self.LoanRequests = []
        self.Offers = []

    def Add_Loan_Request(self, LoanRequest):
    	if self.Type == 'Borrower':
    		self.LoanRequests.append(LoanRequest)
    	else:
    		raise Exception('an Investor Cannot perform this request')
    def Add_Offer(self, Offer):
    	if self.Type == 'Investor':
    		if self.Balance >= Offer.Amount + Offer.Lenmo_Fees:
    			self.Offers.append(Offer)
    		else:   
    			raise Exception('Insufficient Funds')
    	else:
    		raise Exception('a Borrower Cannot perform this request')


    def Get_User_Type(self):
    	return self.Type

    def Get_UserName(self):
   		return str(self.Username)

    def Get_User_Loans(self):
    	if self.Type == 'Borrower':
    		return self.LoanRequests
    	else:
    		return self.Offers

class LoanRequest:
    def __init__(self, Borrower, Amount, Period):
        self.ID = uuid.uuid4()
        self.Borrower = Borrower	
        self.Amount = Amount
        self.Period = Period	
    def getAmount(self):
    	return self.Amount
    def getPeriod(self):
    	return self.Period
    def __str__(self):
    	return "Loan_Request_ID: {},\nBorrower: {},\nAmount: {},\nPeriod: {}\n".format(self.ID, self.Borrower, self.Amount,self.Period)


class Offer:
    def __init__(self, Loan_Request_ID, Investor, Amount, Period, Interest):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request_ID
        self.Investor = Investor	
        self.Amount = Amount
        self.Period = Period		
        self.Interest = Interest
        self.Lenmo_Fees = 3
    def get_Amount(self):
    	return self.Amount
    def get_Period(self):
    	return self.Period
    def get_Interest(self):
    	return self.Interest
    def get_Investor(self):
    	return self.Investor
    def __str__(self):
    	return"Offer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\nAmount: {},\nPeriod: {},\nInterest: {}\n".format(self.ID, self.Loan_Request_ID, self.Investor, self.Amount,self.Period, self.Interest)

class Loan:
    def __init__(self,Loan_Request, Offer, Status):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request.ID
        self.Borrower = Loan_Request.Borrower
        self.Offer_ID = Offer.ID
        self.Investor = Offer.Investor	
        self.Amount = Offer.Amount
        self.Period = Offer.Period		
        self.Interest = Offer.Interest 
        self.Status = Status
    def Schedule_Loan_Payments(self):
        Loan_Payments = []
        Todays_Date = 1 #Assume it's January
        for i in range (self.Period):
            Loan_Payments.append(LoanPayment(self, Todays_Date + 1))
            Todays_Date+=1
            
        return Loan_Payments
    def Get_Status(self):
    	return self.Status
    def __str__(self):
    	return"Loan_ID: {},\nOffer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\nBorrower: {},\nAmount: {},\nPeriod: {},\nInterest: {},\nStatus: {}\n".format(self.ID,self.Offer_ID, self.Loan_Request_ID, self.Investor, self.Borrower, self.Amount,self.Period, self.Interest, self.Status)


class LoanPayment:
    def __init__(self,Loan, Due_Date):
        self.ID = uuid.uuid4()
        self.Loan = Loan
        self.Due_Date = Due_Date
    def Get_Due_Date(self):
        return self.Due_Date
    def __str__(self):
        return"Payment_ID: {},\nLoan_ID: {},\nInvestor: {},\nBorrower: {},\nDue Date: {}\n".format(self.ID, self.Loan.ID, self.Loan.Investor, self.Loan.Borrower, self.Due_Date)










