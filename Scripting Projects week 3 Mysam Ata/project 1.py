Taxrate = 0.20
Standard = 10000.0
Dependant = 3000.
Gross = float(input("Enter gross income: "))
numDependents = int(input("Enter number of dependents: "))

taxableIncome = Gross - Standard - \
Dependant * numDependents
incomeTax = taxableIncome * Taxrate
incomeTax = round(incomeTax, 2)
print ("The income tax is $" + str(incomeTax))
