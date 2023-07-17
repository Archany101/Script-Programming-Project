filename = input('Enter input filename: ')
try:
    file_input = open(filename, 'r')
    print('%-15s%-10s%-10s'%('Name', 'Hours', 'Total Pay'))
    for line in file_input.readlines():
        data = line.split()
        name = str(data[0])
        hours = int(data[1])
        rate = float(data[2])
        pay = hours * rate
        print('%-15s%-10d%-10.2f'%(name, hours, pay))
    file_input.close()
except:
    print('Error while opening file : ', filename);
    exit()
