

# Function creation
def cash_flow(rental_income, operating_expenses):
    return rental_income - operating_expenses

def find_roi(property_value, rental_income, op_expenses, years):
    total_cash_flow = cash_flow(rental_income, op_expenses) * years #ROI formula 
    total_investment = property_value
    return (total_cash_flow / total_investment) * 100


property_value = float(input("Property value: "))
rental_income = float(input("Monthly rental income: "))
op_expenses = float(input("Monthly operating expenses: "))
years = int(input("Number of years owned: "))# no float here its years 


roi = find_roi(property_value, rental_income, op_expenses, years)
print(f"Return on Investment (ROI) for this property: {roi:.2f}%") 
# I googled thwe above part not sure if this is how to call the function here for user input or nopt but it works