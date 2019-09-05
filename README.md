# Lenmo Task

This is my implementation for an assigned task for lenmo.mobi

## Task Description

A Lenmo borrower would like to borrower $5,000.00 on paying them back on 6 months period. One of Lenmo investors has offered him 15% Annual Interest Rate. A $3.00 Lenmo fee will be added to the total loan amount to be paid by the investor. 

### Required Flow

1. The borrower submits a loan request including the above loan amount and loan period 

2. The investor will submit an offer with the above interest rate

3. The borrower will accept the offer

4. Check if the investor has sufficient balance in their account before they fund the loan

5. The loan will be funded successfully and the loan status will be changed to `Funded`

6. The loan payment will be scheduled successfully on the system

7. Once all the payments are successfully paid, the loan status will be `Completed` 


### Runing the Use Case

```
python3 use_case.py
```

Output will start displaying on the terminal with a delay between each of the above requiremnts. This is done to simulate a period of time between the actions


## Running the tests
Run the Automated Unit tests

```
python3 test.py
```



