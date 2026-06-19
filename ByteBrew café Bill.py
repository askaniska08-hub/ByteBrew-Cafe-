print("Welcome to ByteBrew café !")
n=120
print("-"*n)

print("MENU")
print("~"*4)

print("\nLatte      - Rs 150")
print("Cappuccino - Rs 100")
print("Mocha      - Rs 120")
print("Macchiato  - Rs 200")

print("-"*n)

Menu = {"Latte" : 150 , "Cappuccino" : 100 , "Mocha": 120 , "Macchiato" : 200}
order = input("ENTER ITEM NAME :")
if order in Menu:
        amount = Menu[order]
        print("PRICE PER ITEM :", amount)
else: exit(print("Sorry, Item not available"))

quantity = int(input("ENTER QUANTITY :"))
apply_discount = (input("APPLY DISCOUNT? (True/False) :"))


print("-" * n)

print("BILL SUMMARY")
print("~"*12)
subtotal =(quantity * amount)
print("\nSUBTOTAL :", subtotal)

if apply_discount=="True":
        print("DISCOUNT APPLIED : 10%")
        tax = print("TAX : 5%")

        DISCOUNT = (subtotal - (10/100 * subtotal))
        TAX = (DISCOUNT + (DISCOUNT * 5/100))


else:
        print("NO DISCOUNT APPLIED")
        print("TAX : 5%")

        TAX = (subtotal + (subtotal * 5/100))

print("\nFINAL BILL : ", TAX )


print("-"*n)
print("Thank You, Visit Again".center(n))
print("-"*n)
