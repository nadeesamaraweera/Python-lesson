def calculate_cost(price, quantity, discount, tax):
    total_price = price * quantity
    
    discounted_price = total_price - (total_price * discount / 100)
    
    final_price = discounted_price + (discounted_price * tax / 100)
     
    return final_price

price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))
discount = float(input("Enter the discount percentage: "))
tax = float(input("Enter the tax percentage: "))

final_price = calculate_cost(price, quantity, discount, tax)

print(final_price)