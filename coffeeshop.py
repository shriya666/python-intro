


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


total_price=0


order=input("Order Here or Type 'exit' to exit ")

while order!="exit":
    total_price+=Menu[order]
    order=input("Order Here or Type 'exit' to exit ")

print("Total Price: $", total_price)
    

