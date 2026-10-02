product = input("Enter your selected product: ")
cost = float(input("How much was its costs?: "))
amount = int(input("How many products did you buy?: "))

print(f"You have {amount} {product}")

subtotal = cost * amount
total = cost * amount

if amount >= 6:
    total = subtotal - (subtotal * 0.10)
    print("Congratulations, you get a 10% discount")
elif subtotal > 150000:
    total = subtotal - (subtotal * 0.07)
    print("Congratulations, you get a 7% discount")
else: 
    print("Not have any discounts")
    
print (f"So far the price is this: {subtotal}")
print(f"Now your total is: {total}")

