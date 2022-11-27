import numpy as np
import pylab as plt

sales_price = float(input('Enter sales price of house Rs. : '))
Down_Payment = float(input('Enter down payment as a percentage of sales price, e.g. 5 for 5%: '))

Loan_Amount = sales_price*(1-Down_Payment/100)

Mortgage_Type = float(input('Enter mortgage type in years, e.g. 15 for 15 years: '))

Loan_Term = int(12*Mortgage_Type)

Interest_Rate = float(input('Enter loan interest rate as a percentage, e.g 5 for 5%: '))

R = 1 + (Interest_Rate)/(12*100)
X = Loan_Amount*(R**Loan_Term)*(1-R)/(1-R**Loan_Term)

Monthly_Interest =[]
Monthly_Balance = []

for i in range(1, Loan_Term+1):
    Interest = Loan_Amount*(R-1)
    Loan_Amount = Loan_Amount - (X-Interest)
    Monthly_Interest.append(Interest)
    Monthly_Balance.append(Loan_Amount)


print("the home sales price is: " +str('Rs.')+ str(sales_price))
print("the down payment as a percentage of sales price is: =" + str(Down_Payment) + str(' %'))
print("the loan amount is: = "+ str(sales_price*(1-Down_Payment/100)))
print("the interest rate on annual percentage basis is: = " + str(Interest_Rate) + str(' %'))
print("the duration of this loan, that is the loan term (in months) is := " + str(Loan_Term) + str('months'))
print("monthly payment for this mortgage(p & I) is: =" +str('Rs.') + str(np.round(X,2)))
print("Total interset paid over life cycle of the loan is: =" +str('Rs.') + str(np.round(np.sum(Monthly_Interest),2)))


plt.subplot(2, 1, 1)
plt.plot(range(1, Loan_Term+1),Monthly_Interest, 'r', lw=2)
plt.xlabel('month')
plt.ylabel('monthly interest (Rs.)')
plt.subplot(2, 1, 2)
plt.plot(range(1,Loan_Term+1),Monthly_Balance,'b',lw=2)
plt.xlabel('month')
plt.ylabel('monthlly loan balance (Rs.)')
plt.show()