File = input("Enter the name of file you want to copy: ")
copyfile = input("Enter the name of file where you want to copy: ")
with open(File, 'r') as file1, open(copyfile, 'w') as file2:
    data = file1.read()
    file2.write(data)
print("Content of input file is successfully copied!!")
