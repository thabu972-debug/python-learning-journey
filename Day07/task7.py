order_amount = 250
if order_amount >=500:
    discount = order_amount * 20 / 100
    final_amount = order_amount - discount
    print("Order Amount:", order_amount)
    print("Discount:",discount)
    print("Final Amount to pay:",final_amount)
elif order_amount >= 300:
    discount = order_amount * 10 / 100
    final_amount = order_amount - discount
    print("Order Amount:", order_amount)
    print("Discount:",discount)
    print("Final Amount to pay:",final_amount)
elif order_amount >= 100:
    discount = order_amount * 5 / 100
    final_amount = order_amount - discount
    print("Order Amount:", order_amount)
    print("Discount:",discount)
    print("Final Amount to pay:",final_amount)
else:
    print("order Amount:", order_amount)
    print("Discount:",0)
    print("Final Amount to pay:",order_amount)