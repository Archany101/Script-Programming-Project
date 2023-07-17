def printAll(seq):
    print(f"seq: {seq}")
    if seq:
        print(seq[0])
        printAll(seq[1:])

printAll("hello")
printAll((1, 2, 3, 4))
printAll([5, 6, 7, 8, 9])
