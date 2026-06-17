print("Welcome to ByteBrew café")

Menu = ["Latte" , "Cappuccino" , "Mocha" , "Macchiato" ]
order = input("ENTER ITEM NAME :")
if order in Menu:
        print("ITEM AVAILABLE")
else: exit(print("ITEM NOT AVAILABLE"))

quantity = int(input("ENTER QUANTITY :"))
amount = float(input("ENTER PRICE PER ITEM :"))
discount = bool(input("APPLY DISCOUNT? (YES/NO) :"))

if discount:
    discount == NO
    subtotal =(quantity * amount)
    print("SUBTOTAL :", subtotal)
    tax = print("TAX : 5%")

    TAX = (subtotal + (subtotal * 5/100))
    print("FINAL BILL :", TAX)

else:
    subtotal =(quantity * amount)
    print("SUBTOTAL :", subtotal)
    discount = print("DISCOUNT APPLIED : 10%")
    tax = print("TAX : 5%")

DISCOUNT = (subtotal - (10/100 * subtotal))
TAX = (DISCOUNT + (DISCOUNT * 5/100))
print("FINAL BILL :", TAX)