# 1. calculate_discount(price, discount_percent) If the discount is 20% or higher, 
# apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:    
        return price
print(calculate_discount(100, 20))  # Output: 100 (Discount is less than 20%, so no discount applied)

# 2. Using the calculate_discount function, prompt the user to enter the original price of an item and the 
# discount percentage. Print the final price after applying the discount, or if no discount was applied, 
# print the original price.

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying the discount is: {final_price}")


