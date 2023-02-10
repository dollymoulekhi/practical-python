# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, 
# Stock Investment, and Bitcoin trading corporation. 
# The interest rate is 5% and the monthly payment is $2684.11.

# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

# Exercise 1.8: Extra payments
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# Modify the program to incorporate this extra payment and have it print the total amount paid along with the 
# number of months required.
# When you run the new program, it should report a total payment of 929,965.62 over 342 months.

total_pay=500000
monthly_pay=2684.11
i=0
total_payed=0
while total_pay> 0:
    i=i+1
    if i<=12:
        monthly_pay=3684.11
    elif i>12:
       monthly_pay= 2684.11   
    intrest_pay=total_pay*5/1200
    remaining_mon=monthly_pay - intrest_pay
    total_pay=total_pay-remaining_mon
    total_payed=monthly_pay*i

total_payed=3684.11*12 +(2684.11)*(i-12)
print(i)
print(total_payed)
