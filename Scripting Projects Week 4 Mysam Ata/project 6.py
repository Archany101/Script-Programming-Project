pi=1
denom=3
iterate=int(input('Enter # of iterations: '))
if iterate==1:
    value=1
else:
    for i in range(iterate-1):
        pi=pi+(1/denom)*((-1)**(i+1))
        denom=denom+2
print('value of pi is:)', pi)
