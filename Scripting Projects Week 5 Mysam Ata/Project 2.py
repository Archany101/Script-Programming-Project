side1=int(input('Enter first side: ')) 
side2=int(input('Enter second side: ')) 
side3=int(input('Enter third side: '))
if (side1*side1+side2*side2)==side3*side3 or (side1*side1+side3*side3)==side2*side2 or (side2*side2+side3*side3)==side1*side1:
    print('This is a right triangle.') 
else:
    print('This is not a right triangle.') 
