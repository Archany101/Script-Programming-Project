encryption = input("Enter the coded text: ")
key = int(input("Enter the distance value: "))
real = ""
for ch in encryption:
    real += chr(ord(ch)-key)
print()
print(real)
