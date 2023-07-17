maxval=126
minval=32
distance=maxval-minval+1
text=input("enter text: ")
distance=int(input("enter distance: "))
encryption= ""
for i in text:
    value=ord(i)
    cvalue=value+distance
    cvalue=cvalue % distance
    if cvalue <minval:
        cvalue += distance
        encryption += chr(cvalue)
print (encryption)
