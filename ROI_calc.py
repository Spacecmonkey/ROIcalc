

# Function creation
def calculate_cash_flow(rental_income, operating_expenses):
    return rental_income - operating_expenses

def calculate_roi(property_value, rental_income, operating_expenses, years_held):
    total_cash_flow = calculate_cash_flow(rental_income, operating_expenses) * years_held
    total_investment = property_value
    return (total_cash_flow / total_investment) * 100


property_value = float(input("Property value: "))
rental_income = float(input("Monthly rental income: "))
operating_expenses = float(input("Monthly operating expenses: "))
years_held = int(input("Number of years owned: "))# no float here its years 


roi = calculate_roi(property_value, rental_income, operating_expenses, years_held)
print(f"Return on Investment (ROI) for this property: {roi:.2f}%") 
# I googled thwe above part not sure if this is how to call the function here for user input or nopt but it works