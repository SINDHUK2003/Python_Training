def expense_tracker(lst):

    total = 0
    minimum = lst[0]
    maximum = lst[0]

    for x in lst:
        total += x

        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x 

    n = len(lst)
    average = int(total/n)

    result = {
        "Total" : total,
        "Average" : average,
        "Minimum" : minimum,
        "Maximum" : maximum
    }

    return result

expense_lst = []

days = int(input("Enter the number of days: "))
x = 1
while(x <= days):
    print(f"Enter the expense of day{x}: ")
    expenses_per_day = int(input())
    if expenses_per_day < 0:
        print("Enter a valid expense")
        continue
    expense_lst.append(expenses_per_day)
    x += 1

rslt = expense_tracker(expense_lst)

print("Expense Report")
print("Total: ", rslt["Total"])
print("Average: ", rslt["Average"])
print("Minimum: ", rslt["Minimum"])
print("Maximum: ", rslt["Maximum"])






