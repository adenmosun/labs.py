def tax_compiler(yearly_income):
    if (yearly_income >= 0) and (yearly_income <= 1000):
        return 0
    if (yearly_income > 1000) and (yearly_income <= 10000):
        return (0.1 * (yearly_income-1000))
    if (yearly_income > 10000) and (yearly_income <= 20200):
        return ((0.1*(10000-1000)) + (0.15*(yearly_income-10000)))
    if (yearly_income > 20200) and (yearly_income <= 30750):
        return ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(yearly_income-20200)))
    if (yearly_income > 30750) and (yearly_income <= 50000):
        return ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(yearly_income-30750)))
    if (yearly_income > 50000):
        return ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(50000-30750)) + (0.3*(yearly_income-50000)))
    return 0

def calculate_tax(employees):
    try:
        emp_tax = {}
        for k, v in employees.items():
            emp_tax[k] = tax_compiler(v)
    except (AttributeError,TypeError):
        raise ValueError("The provided input is not a dictionary.")
    return(emp_tax)



yi = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000
}


print(calculate_tax(yi))
	
