filename = input("Enter the input file name: ")
try:
    f = open(filename, 'r')
except FileNotFoundError:
    print('No file found')
    exit()
lines = f.read().splitlines()
f.close()
print()
while(True):
    print(f"The file has {len(lines)} lines")
    try:
        lineNumber = int(input("Enter a line number [0 to quit]: "))
    except ValueError:
        print('ERROR: you must enter a number.')
        continue
    if (lineNumber > len(lines)):
        print(f'ERROR: line number must be less than {len(lines)}.')
        continue
    if (lineNumber < 0):
        print(f'ERROR: line number must be greater than 0.')
        continue
    if (lineNumber == 0):
        break
    print(f'{lineNumber} : {lines[lineNumber-1]}')
