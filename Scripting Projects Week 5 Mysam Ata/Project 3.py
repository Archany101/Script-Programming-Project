import random
import math
small=int(input("Enter small number: "))
large=int(input("Enter large number: "))
num=int(input("Enter any number between: "))
print("Minimum number of guesses:",int((large-small+1)))
count=0
while True:
    count+=1
mid=random.randint(small,large)
print(mid)
if mid<num:
    print("Too small")
    small=mid
elif mid>num:
    print("Too big")
    large=mid
else:
    print("Computer guessed it in",count,"tries")
    
