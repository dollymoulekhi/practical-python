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

# Exercise 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally handled. 
# Make it so that the user can set these variables:

# Exercise 1.10: Making a table
# Modify the program to print out a table showing the month, 
# total paid so far, and the remaining principal. The output should look something like this:


import pdb
extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000
total_pay=500000
monthly_pay=2684.11
i=0
total_payed=0
while total_pay> 0:
    if total_pay< monthly_pay:
        break
    else: 
    # pdb.set_trace()
        i=i+1
        if i>=extra_payment_start_month and i<=extra_payment_end_month:
            changed_pay=monthly_pay+extra_payment
            intrest_pay=total_pay*5/1200
            remaining_mon=changed_pay - intrest_pay
            total_pay=total_pay-remaining_mon
            total_payed=changed_pay+total_payed
            print(i,total_payed,total_pay )
        else:
            monthly_pay= monthly_pay
            intrest_pay=total_pay*5/1200
            remaining_mon=monthly_pay - intrest_pay
            total_pay=total_pay-remaining_mon
            total_payed=monthly_pay+total_payed
            print(i,total_payed,total_pay )
# print(i)
# print(total_payed)
