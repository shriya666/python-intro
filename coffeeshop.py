


Menu={
    "Latte" : 3,
    "Black Coffee": 3,
    "Green Tea": 3.50,
    "Milk Tea": 3.50,
    "Frappe": 4,
    "Croissant": 4,
    "Eclair": 2,
    "Baguette": 5,
    "Macarons": 10,
    "Cheese Platter": 7,
}
print("Menu")
for item, price in Menu.items():
    print(item,": $", price)

sales_tax= 1.0725
total_price=0

reciept={

}
order=input("Order Here or Type 'exit' to exit ")

while order!="exit":
    num=int(input("How many of this item? "))
    total_price+=Menu[order]*num
    reciept[order + ' x ' + str(num)] = round((Menu[order]*num), 2)
    order=input("Order Here or Type 'exit' to exit ")


subtotal= total_price


print("Total Price: $", total_price)
print("Receipt")
for item, price in reciept.items():
    print(item,": $", price)
    print("Subtotal: ", "$", subtotal)
