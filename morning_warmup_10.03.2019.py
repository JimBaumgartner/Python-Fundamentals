def calculate_savings(prev_price, current_price, amount, tax):
    """
    10.03.2019
    Function's purpose is to calculate and report savings on a purchase
​    prev_price          (float number describing the price befores savings)
    current_price       (float number describing the price at purchasing)
    amount              (int number denoting how many were purchased)
    tax                 (float number describing the state's tax percentage)
    This function should return a float number describing how much was saved
    or a string stating "no savings occurred"
    """
    tax_percentage = 1 + tax
    previous_total = ((prev_price * amount) * tax_percentage)
    current_total = (current_price * amount) * tax_percentage
    savings = (previous_total - current_total)
    return savings if savings > 0 else "No Savings Occurred"
"""
You must return to get anything out if def function
"""
tax = .08
prev_price = 20
current_price = 10
amount = 1

answer = calculate_savings(prev_price, current_price, amount, tax)
print(answer)

