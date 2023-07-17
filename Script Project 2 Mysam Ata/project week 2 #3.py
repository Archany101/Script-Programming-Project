new=int(input("Enter number of new videos for rent: "))
old=int(input("Enter number of old videos for rent: "))
nights=int(input("Enter number of nights you want to rent: "))
total=(new*3+old*2)*nights
print("Total charge: $"+str(total))
