import unittest
from models import *
Borrower = User('Borrower', 'Lotfy', 0)
Investor =	User('Investor', 'Ahmed', 20000)	
Loan_Request = LoanRequest(Borrower.Get_UserName(), 5000, 6)
Offer = Offer(Loan_Request.ID, Investor.Get_UserName(), 5000, 6, 15)

class TestModels(unittest.TestCase):
	def test_Add_Loan_Request(self):
		Borrower.Add_Loan_Request(Loan_Request)
		self.assertEqual(Borrower.LoanRequests[0], Loan_Request, "Should be the same")
	def test_Add_offer(self):
		Investor.Add_Offer(Offer)
		self.assertEqual(Investor.Offers[0], Offer, "Should be the same")
	def test_Get_User_Type(self):
		self.assertEqual(Investor.Get_User_Type(), 'Investor', "Should be the same")
		self.assertEqual(Borrower.Get_User_Type(), 'Borrower', "Should be the same")
	def test_Get_UserName(self):
		self.assertEqual(Investor.Get_UserName(), 'Ahmed', "Should be the same")
		self.assertEqual(Borrower.Get_UserName(), 'Lotfy', "Should be the same")
	def test_Loan_Request_Get_Amount(self):
		self.assertEqual(Loan_Request.Get_Amount(), 5000, "Should be the same")
	def test_Loan_Request_Get_Period(self):
		self.assertEqual(Loan_Request.Get_Period(), 6, "Should be the same")
	def test_Offer_Get_Amount(self):
		self.assertEqual(Offer.Get_Amount(), 5000, "Should be the same")
	def test_Offer_Get_Period(self):
		self.assertEqual(Offer.Get_Period(), 6, "Should be the same")
	def test_Offer_Get_Interest(self):
		self.assertEqual(Offer.Get_Interest(), 15, "Should be the same")
	def test_Loan_Status_After_Offer(self):
		self.Loan = Loan(Loan_Request,Offer)
		self.assertEqual(self.Loan.Get_Status(), 'Funded', "Should be the same")
	def test_Loan_Payments_Array(self):
		self.Loan = Loan(Loan_Request,Offer)
		self.assertEqual(self.Loan.Get_Loan_Payments(), self.Loan.Schedule_Loan_Payments(), "Should be the same")
	def test_Loan_Payments_Amount(self):
		self.Loan = Loan(Loan_Request,Offer)
		self.Loan_Payments = self.Loan.Get_Loan_Payments()
		for i in range (len(self.Loan_Payments)):
			self.assertEqual(self.Loan_Payments[i].Get_Amount(), 896, "Should be the same")
	def test_Loan_Payments_Status(self):
		self.Loan = Loan(Loan_Request,Offer)
		self.Loan_Payments = self.Loan.Get_Loan_Payments()
		for i in range (len(self.Loan_Payments)):
			self.assertEqual(self.Loan_Payments[i].Get_Status(), 'Due', "Should be the same")
	def test_Loan_Status_After_Payments(self):
		self.Loan = Loan(Loan_Request,Offer)
		self.Loan_Payments = self.Loan.Get_Loan_Payments()
		for i in range (len(self.Loan_Payments)):
			self.Loan_Payments[i].Update_Status('Paid') 
		self.Loan.Update_Status()
		self.assertEqual(self.Loan.Get_Status(), 'Completed', "Should be the same")
if __name__ == '__main__':
	unittest.main()