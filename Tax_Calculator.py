import streamlit as st

def f1_opt_tax_calculator(income, state_tax_rate=0.05, student_loan_interest=0, moving_expenses=0):
    """
    Calculates estimated federal and state taxes for an F1 OPT student (Indian national).
    """
    
    # Standard Deduction for Indian F1 OPT Students (2024)
    STANDARD_DEDUCTION = 14600
    
    # Additional Deductions (Capped by IRS Limits)
    student_loan_interest = min(student_loan_interest, 2500)
    
    # Calculate Taxable Income
    taxable_income = max(0, income - STANDARD_DEDUCTION - student_loan_interest - moving_expenses)
    
    # Federal Tax Brackets (2024) for Single Filers
    federal_brackets = [
        (0, 11600, 0.10),
        (11600, 47150, 0.12),
        (47150, 100525, 0.22),
        (100525, 191950, 0.24),
        (191950, 243725, 0.32),
        (243725, 609350, 0.35),
        (609350, float('inf'), 0.37)
    ]
    
    # Federal Tax Calculation
    federal_tax = 0
    for lower, upper, rate in federal_brackets:
        if taxable_income > lower:
            taxed_amount = min(taxable_income, upper) - lower
            federal_tax += taxed_amount * rate
    
    # State Tax Calculation
    state_tax = taxable_income * state_tax_rate
    
    return {
        "Income": income,
        "Taxable Income": taxable_income,
        "Federal Tax": round(federal_tax, 2),
        "State Tax": round(state_tax, 2),
        "Total Tax": round(federal_tax + state_tax, 2),
        "Effective Tax Rate": round(((federal_tax + state_tax) / income) * 100 if income > 0 else 0, 2)
    }

# Streamlit UI
st.title("F1 OPT Tax Calculator")

income = st.number_input("Enter your annual income ($):", min_value=0, value=75000)
state_tax_rate = st.number_input("Enter your state tax rate (%):", min_value=0.0, max_value=0.1, value=0.05) / 100
student_loan_interest = st.number_input("Enter student loan interest paid ($):", min_value=0, max_value=2500, value=2000)
moving_expenses = st.number_input("Enter moving expenses ($):", min_value=0, value=1000)

if st.button("Calculate Tax"):
    result = f1_opt_tax_calculator(income, state_tax_rate, student_loan_interest, moving_expenses)
    st.write("### Tax Breakdown")
    st.write(result)
