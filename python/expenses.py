expenses = [10.50, 8, 15, 20, 5, 3]
jod = 0

for expense in expenses:
    jod += expense


print("You spent a sum of : $", jod, " USD", sep='')
print("You spent a sum of : $", sum(expenses), " USD", sep='')


total = 0
kharche = []

for i in range(7):
    kharche.append(float(input("कहाँ क्या खर्चा किया ?")))

total = sum(kharche)

print("total kharche ₹", total, sep='')
