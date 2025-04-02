def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    price = integer(input("2500 "))
discount_percent = float(input("25.2 "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: ${final_price:.2f}")
if final_price == price:
    print(f"No discount applied. The price remains: ${price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")