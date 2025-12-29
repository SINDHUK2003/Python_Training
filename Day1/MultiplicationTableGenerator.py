Table = int(input("Enter Multiplication Table: "))
Range = int(input("Enter Table Range: "))

for x in range(1, Range + 1):
    print(x, 'x', Table, '=', (x * Table))
