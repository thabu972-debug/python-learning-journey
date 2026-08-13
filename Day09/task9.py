#task 1

def show_banner():
    print("Hey buddy")
    print("How are you")
    print("How is your day")
show_banner()

#task 2

def show_shop_info(shop,location,delivery):
    print("shop:",shop)
    print("location:",location)
    print("delivery:",delivery)
show_shop_info("SM Veg Mart","Puducherry","Same day")

#task 3

def greet_customer(name,city):
    print("name:",name)
    print("city:",city)
greet_customer("Meena", "Chennai")
greet_customer("Ravi", "Puducherry")
greet_customer("Anitha", "Coimbatore")

#task 4

def show_delivery_charge(order_amount):
    if order_amount >= 300:
        print("Free delivery!")
    else:
        print("Delivery charge: Rs 40")

# Calling the function
show_delivery_charge(450)  
show_delivery_charge(150)  
show_delivery_charge(300)  

#task 5

def calculate_bill(price, quantity):
    return price * quantity

# Calling the function and printing the result
bill1 = calculate_bill(45, 3)
print("Total bill: Rs", bill1)  

bill2 = calculate_bill(120, 2)
print("Total bill: Rs", bill2)  