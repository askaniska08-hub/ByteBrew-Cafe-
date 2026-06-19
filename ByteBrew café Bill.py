print("Welcome to ByteBrew café !")
n=120
print("-"*n)

print("MENU \n")

print("Latte      - Rs 150")
print("Cappuccino - Rs 100")
print("Mocha      - Rs 120")
print("Macchiato  - Rs 200")

print("-"*n)

Menu = ["Latte" , "Cappuccino" , "Mocha" , "Macchiato" ]
order = input("ENTER ITEM NAME :")
if order in Menu:
        print("Order accepted")
else: exit(print("Sorry, Item not available"))

quantity = int(input("ENTER QUANTITY :"))
amount = float(input("ENTER PRICE PER ITEM :"))
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
