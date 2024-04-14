def calculate_discount(price, discount_percent):
    discount = discount_percent / 100
    if discount >= 0.2:
        final_price= price * (1 - discount)
    else:
        final_price = price
    return final_price

original_price = float(input("Original price of the item: "))
discount_percent = float(input("discount_percent(0-100): "))
final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount: {discount_percent:2f}%")
    print(f"Final price after dicount: ${final_price: .2f}")
else:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount: {discount_percent:.2f}%")
    print(f"Final Price: ${original_price:.2f}")



