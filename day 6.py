total = 0

count = int(input("How many sales? "))

for i in range(count):
    sale = int(input("Enter sale amount: "))
    total = total + sale

expenses = int(input("Enter total expenses: "))

profit = total - expenses

print("Total sales:", total)
print("Expenses:", expenses)

if profit > 0:
    print("Profit:", profit)
elif profit < 0:
    print("Loss:", profit)
else:
    print("Break even")