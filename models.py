###########################################################
#Created By Lotfy Abdel Khaliq on 04/09/2019
###########################################################
import uuid
import datetime
import calendar


###########################################################
# User Class Definition
class User:
    """
    User class holds the important info of each user on the system.
    It's intialized by the Type of the user (Investor/Borrower), Username and Balance
    """    
    def __init__(self, Type, Username, Balance):
        self.ID = uuid.uuid4() #Unique ID
        self.Type = Type
        self.Username = Username
       	self.Balance = Balance
        self.LoanRequests = []
        self.Offers = []
        self.Loans = []

    def Add_Loan_Request(self, LoanRequest):
        """
        This function appends a loan request to the list of this user's loan requests, 
        but it first checks if he's logged in as a Borrower.
        """   
        if self.Type == 'Borrower':
        	self.LoanRequests.append(LoanRequest)
        else:
        	raise Exception('an Investor Cannot perform this request')
    def Add_Offer(self, Offer):
        """
        This function appends an offer to the list of this user's offers, 
        but it first checks if he's logged in as an Investor & he has enough balance.
        """   
        if self.Type == 'Investor':
        	if self.Balance >= Offer.Amount + Offer.Lenmo_Fees:
        		self.Offers.append(Offer)
        	else:   
        		raise Exception('Insufficient Funds')
        else:
        	raise Exception('a Borrower Cannot perform this request')
    def Add_Loan(self, Loan):
        """
        This function appends a loan to the list of this user's loans, 
        """   
        self.Loans.append(Loan)
    def Get_User_Type(self):
    	return self.Type
    def Get_UserName(self):
   		return self.Username
    def Get_User_Loan_Requests(self):
        """
        This function returns a list of this user's loan requests, 
        but checks first if he's a Borrower
        """   
        if self.Type == 'Borrower':
            return self.LoanRequests
        else:
            raise Exception('an Investor Cannot perform this request')
    def Get_User_Offers(self):
        """
        This function returns a list of this user's offers, 
        but checks first if he's an Investor
        """  
        if self.Type == 'Investor':
            return self.Offers
        else:
            raise Exception('a Borrower Cannot perform this request')
    def Get_User_Loans(self):
        return self.Loans
###########################################################
# Loan Request Class Definition
class LoanRequest:
    """
    LoanRequest class holds the details of a loan request
    it has some gtters to get these details for later use 
    """  
    def __init__(self, Borrower, Amount, Period):
        self.ID = uuid.uuid4()
        self.Borrower = Borrower	
        self.Amount = Amount
        self.Period = Period	
    def Get_Amount(self):
    	return self.Amount
    def Get_Period(self):
    	return self.Period
    def __str__(self):
        '''
        This function is used for printing the details of the LoanRequest object
        '''
        return "Loan_Request_ID: {},\nBorrower: {},\nAmount: ${},\nPeriod: {}\n".format(self.ID, self.Borrower, self.Amount,self.Period)
###########################################################
# Offer Class Definition
class Offer:
    """
    Offer class holds the details of an offer made by the investor
    it has some gtters to get these details for later use 
    """  
    def __init__(self, Loan_Request_ID, Investor, Amount, Period, Interest):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request_ID
        self.Investor = Investor	
        self.Amount = Amount
        self.Period = Period		
        self.Interest = Interest
        self.Lenmo_Fees = 3 #This is added to any offer's amount
    def Get_Amount(self):
    	return self.Amount
    def Get_Period(self):
    	return self.Period
    def Get_Interest(self):
    	return self.Interest
    def Get_Investor(self):
    	return self.Investor
    def __str__(self):
        '''
        This function is used for printing the details of the Offer object
        '''
        return"Offer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\nAmount: ${},\nPeriod: {},\nInterest: {}%\n".format(self.ID, self.Loan_Request_ID, self.Investor, self.Amount,self.Period, self.Interest)
###########################################################
# Loan Class Definition
class Loan:
    """
    - Loan class takes 3 parameters for instantiation. 
    The first one is a LoanRequest Object, the second one is an offer object,
    and the third one is the status, which is 'Funded' by default

    - It has also a list of Loan Payments which are created according to the amount of the offer, the interest, and the period

    """  
    def __init__(self,Loan_Request, Offer, Status = 'Funded'):
        self.ID = uuid.uuid4()
        self.Loan_Request_ID = Loan_Request.ID
        self.Borrower = Loan_Request.Borrower
        self.Offer_ID = Offer.ID
        self.Investor = Offer.Investor	
        self.Amount = Offer.Amount
        self.Period = Offer.Period		
        self.Interest = Offer.Interest 
        self.Status = Status
        self.Loan_Payments = []
        self.Schedule_Loan_Payments()
    def Schedule_Loan_Payments(self):
        '''
        This function schedules number of payments according to 
        the period in the offer, and put them in Loan Payments array of this class
        Each iteration is a 1-month difference
        '''
        Todays_Date = datetime.date.today()
        for i in range (self.Period):
            self.Loan_Payments.append(LoanPayment(self, Todays_Date))
            Todays_Date = self.Add_Months(Todays_Date, 1)
            
        return self.Loan_Payments
    def Add_Months(self,sourcedate, months):
        '''
        This function changes the date by the variable (months)
        '''
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year,month)[1])
        return datetime.date(year, month, day)
    def Get_Status(self):
    	return self.Status
    def Get_Loan_Payments(self):
        return self.Loan_Payments
    def Update_Status(self):
        '''
        This function changes the status of the loan to 'Completed'
        Once all payments are paid
        '''
        All_Paymments_Recieved = True
        for i in range (len(self.Loan_Payments)):
            if self.Loan_Payments[i].Get_Status() != 'Paid':
                All_Paymments_Recieved = False
        if All_Paymments_Recieved == True:
            self.Status = 'Completed'
    def __str__(self):
        '''
        This function is used for printing the details of the Loan object
        '''
        return"Loan_ID: {},\nOffer_ID: {},\nLoan_Request_ID: {},\nInvestor: {},\nBorrower: {},\nAmount: ${},\nPeriod: {},\nInterest: {}%,\nStatus: {}\n".format(self.ID,self.Offer_ID, self.Loan_Request_ID, self.Investor, self.Borrower, self.Amount,self.Period, self.Interest, self.Status)

###########################################################
# Loan Class Definition
class LoanPayment:
    """
    LoanPayment class holds the details of each Loan Payment 
    it has some gtters to get these details for later use 

    -Loan Monthly Payment Amount calculation takes in consideration the interest:
    First we calculate the Interest per month, and add that to the offer amount divided by the period
    """  
    def __init__(self,Loan, Due_Date, Status = 'Due'):
        self.ID = uuid.uuid4()
        self.Loan = Loan
        self.Due_Date = Due_Date
        self.Amount = round((Loan.Amount/Loan.Period) + (Loan.Interest/(100*12)) * (Loan.Amount))
        self.Status = Status
    def Get_Due_Date(self):
        return self.Due_Date
    def Get_Amount(self):
        return self.Amount
    def Get_Status(self):
        return self.Status
    def Update_Status(self, Status):
        self.Status = Status
    def __str__(self):
        '''
        This function is used for printing the details of the LoanPayment object
        '''
        return"Payment_ID: {},\nLoan_ID: {},\nInvestor: {},\nBorrower: {},\nAmount: ${},\nDue Date: {},\nStatus: {}\n".format(self.ID, self.Loan.ID, self.Loan.Investor, self.Loan.Borrower, self.Amount,self.Due_Date, self.Status)










