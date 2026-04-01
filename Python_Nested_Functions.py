# Nested Function

def calculate_bill(amount):
    """
    Calculates final bill amount including tax and discount
    """

    def apply_tax(value):
        # Adds 18% tax
        return value + (value * 0.18)

    def apply_discount(value):
        # Applies 10% discount if amount > 1000
        if value > 1000:
            return value - (value * 0.10)
        return value

    #  Apply tax
    taxed_amount = apply_tax(amount)

    #  Apply discount
    final_amount = apply_discount(taxed_amount)

    return final_amount


bill = 1200
result = calculate_bill(bill)

print("Final Bill Amount:", result)

"""
Output:
Final Bill Amount: 1274.4
"""
