print("Welcome to ByteBrew café !")

Menu_1 = ("Latte") 
Menu_2 = ("Cappuccino")
Menu_3 = ("Mocha") 
Menu_4= ("Macchiato")
order = input("ENTER ITEM NAME :")

quantity = int(input("ENTER QUANTITY :"))
amount = float(input("ENTER PRICE PER ITEM :"))
discount = input("APPLY DISCOUNT? (True/False) : True")

n = 120
print("-" * n)

subtotal =(quantity * amount)
print("SUBTOTAL :", subtotal)
discount = print("DISCOUNT APPLIED : 10%")
tax = print("TAX : 5%")

DISCOUNT = (subtotal - (10/100 * subtotal))
TAX = (DISCOUNT + (DISCOUNT * 5/100))
print("FINAL BILL :", TAX)
