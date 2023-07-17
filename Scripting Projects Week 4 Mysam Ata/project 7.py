salary = float(input("Enter salary: "))
per = float(input("increase: "))
year = int(input("Years: "))
for i in range(1,year+1):
    print(salary)
    salary = salary * (1+per/100)
