#!/usr/bin/env python3
# Write a program that computes an investment report.

# Getting User inputs:
intialBalance = float(input("ENTER the investment amount :"))
years = int (input("ENTER the number of years : "))
interestRate = int(input("ENTER the rate in PERCENTAGE %:"))

# converting the rate to decimal number
interestRate = interestRate/100

# intializing a variable to keep track of intrest accumulation
totalInterest = 0.0

# Display styling : with print
print("%4s%18s%10s%16s" %("Year","Initial Balance","Interest","Ending Balance"))

for year in range(1, years +1):
    interest = intialBalance * interestRate
    endBalance = intialBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year,intialBalance,interest,endBalance))
    intialBalance = endBalance
    totalInterest += interest

# Display the total totals for the Given period
print("Ending Balance : $%0.2f" % endBalance)
print("Total interest earned : $%0.2f" % totalInterest)    
