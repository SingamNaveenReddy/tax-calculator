import streamlit as st

# Dictionary with simplified state tax information (for demo purposes)
STATE_TAX_INFO = {
    "Alabama": {"type": "brackets", "brackets": [(0, 500, 0.02), (500, 3000, 0.04), (3000, float('inf'), 0.05)]},
    "Alaska": {"type": "flat", "rate": 0.0},
    "Arizona": {"type": "brackets", "brackets": [(0, 10000, 0.0259), (10000, 25000, 0.0334), (25000, 50000, 0.0417), (50000, float('inf'), 0.0450)]},
    "Arkansas": {"type": "brackets", "brackets": [(0, 4290, 0.02), (4290, 8500, 0.04), (8500, 12700, 0.05), (12700, float('inf'), 0.06)]},
    "California": {"type": "brackets", "brackets": [(0, 8809, 0.01), (8809, 20883, 0.02), (20883, 32960, 0.04), (32960, 45753, 0.06), (45753, 57824, 0.08), (57824, 295373, 0.093), (295373, 354445, 0.103), (354445, 590742, 0.113), (590742, float('inf'), 0.123)]},
    "Colorado": {"type": "flat", "rate": 0.0455},
    "Connecticut": {"type": "brackets", "brackets": [(0, 10000, 0.03), (10000, 50000, 0.05), (50000, 100000, 0.055), (100000, 200000, 0.06), (200000, 250000, 0.065), (250000, float('inf'), 0.069)]},
    "Delaware": {"type": "brackets", "brackets": [(0, 2000, 0.022), (2000, 5000, 0.039), (5000, 10000, 0.048), (10000, 20000, 0.052), (20000, 25000, 0.055), (25000, float('inf'), 0.066)]},
    "Florida": {"type": "flat", "rate": 0.0},
    "Georgia": {"type": "brackets", "brackets": [(0, 750, 0.01), (750, 2250, 0.02), (2250, 3750, 0.03), (3750, 5250, 0.04), (5250, float('inf'), 0.05)]},
    "Hawaii": {"type": "brackets", "brackets": [(0, 2400, 0.014), (2400, 4800, 0.028), (4800, 7200, 0.033), (7200, 9600, 0.038), (9600, float('inf'), 0.04)]},
    "Idaho": {"type": "brackets", "brackets": [(0, 1550, 0.01), (1550, 3100, 0.03), (3100, 4650, 0.04), (4650, float('inf'), 0.05)]},
    "Illinois": {"type": "flat", "rate": 0.0495},
    "Indiana": {"type": "flat", "rate": 0.0323},
    "Iowa": {"type": "brackets", "brackets": [(0, 17150, 0.0036), (17150, 32300, 0.0412), (32300, 48500, 0.0525), (48500, float('inf'), 0.0625)]},
    "Kansas": {"type": "brackets", "brackets": [(0, 15000, 0.03), (15000, 30000, 0.05), (30000, float('inf'), 0.057)]},
    "Kentucky": {"type": "flat", "rate": 0.05},
    "Louisiana": {"type": "brackets", "brackets": [(0, 12500, 0.02), (12500, 50000, 0.04), (50000, float('inf'), 0.06)]},
    "Maine": {"type": "brackets", "brackets": [(0, 22000, 0.058), (22000, 52000, 0.0675), (52000, float('inf'), 0.0715)]},
    "Maryland": {"type": "brackets", "brackets": [(0, 1000, 0.02), (1000, 2000, 0.03), (2000, 3000, 0.04), (3000, 100000, 0.0475), (100000, float('inf'), 0.05)]},
    "Massachusetts": {"type": "flat", "rate": 0.05},
    "Michigan": {"type": "flat", "rate": 0.0425},
    "Minnesota": {"type": "brackets", "brackets": [(0, 26770, 0.0535), (26770, 86640, 0.0705), (86640, float('inf'), 0.0785)]},
    "Mississippi": {"type": "flat", "rate": 0.05},
    "Missouri": {"type": "brackets", "brackets": [(0, 108, 0.015), (108, 1044, 0.02), (1044, 2088, 0.025), (2088, float('inf'), 0.03)]},
    "Montana": {"type": "brackets", "brackets": [(0, 3100, 0.01), (3100, 5800, 0.02), (5800, 8700, 0.03), (8700, float('inf'), 0.04)]},
    "Nebraska": {"type": "brackets", "brackets": [(0, 3100, 0.0246), (3100, 18600, 0.0351), (18600, float('inf'), 0.0684)]},
    "Nevada": {"type": "flat", "rate": 0.0},
    "New Hampshire": {"type": "flat", "rate": 0.0},
    "New Jersey": {"type": "brackets", "brackets": [(0, 20000, 0.014), (20000, 35000, 0.0175), (35000, 50000, 0.035), (50000, 75000, 0.05525), (75000, float('inf'), 0.0637)]},
    "New Mexico": {"type": "brackets", "brackets": [(0, 5000, 0.017), (5000, 10000, 0.032), (10000, float('inf'), 0.049)]},
    "New York": {"type": "brackets", "brackets": [(0, 8500, 0.04), (8500, 11700, 0.045), (11700, 13900, 0.0525), (13900, 21400, 0.059), (21400, 80650, 0.0621), (80650, 215400, 0.0649), (215400, 1077550, 0.0685), (1077550, float('inf'), 0.0882)]},
    "North Carolina": {"type": "flat", "rate": 0.0525},
    "North Dakota": {"type": "brackets", "brackets": [(0, 4050, 0.011), (4050, 12150, 0.022), (12150, float('inf'), 0.029)]},
    "Ohio": {"type": "brackets", "brackets": [(0, 22000, 0.0027), (22000, 44000, 0.0033), (44000, 88000, 0.0038), (88000, 110000, 0.0045), (110000, float('inf'), 0.0048)]},
    "Oklahoma": {"type": "brackets", "brackets": [(0, 1000, 0.005), (1000, 2500, 0.01), (2500, 3750, 0.02), (3750, float('inf'), 0.03)]},
    "Oregon": {"type": "brackets", "brackets": [(0, 3650, 0.04), (3650, 9200, 0.06), (9200, 125000, 0.08), (125000, float('inf'), 0.09)]},
    "Pennsylvania": {"type": "flat", "rate": 0.0307},
    "Rhode Island": {"type": "brackets", "brackets": [(0, 66650, 0.0375), (66650, 166000, 0.0475), (166000, float('inf'), 0.0599)]},
    "South Carolina": {"type": "brackets", "brackets": [(0, 3000, 0.0), (3000, 6000, 0.03), (6000, float('inf'), 0.04)]},
    "South Dakota": {"type": "flat", "rate": 0.0},
    "Tennessee": {"type": "flat", "rate": 0.0},
    "Texas": {"type": "flat", "rate": 0.0},
    "Utah": {"type": "flat", "rate": 0.0495},
    "Vermont": {"type": "brackets", "brackets": [(0, 4000, 0.035), (4000, 8000, 0.06), (8000, 12000, 0.068), (12000, float('inf'), 0.087)]},
    "Virginia": {"type": "brackets", "brackets": [(0, 1700, 0.02), (1700, 2700, 0.03), (2700, 5400, 0.05), (5400, float('inf'), 0.0575)]},
    "Washington": {"type": "flat", "rate": 0.0},
    "West Virginia": {"type": "brackets", "brackets": [(0, 10000, 0.03), (10000, 25000, 0.04), (25000, float('inf'), 0.045)]},
    "Wisconsin": {"type": "brackets", "brackets": [(0, 12000, 0.035), (12000, 24000, 0.055), (24000, float('inf'), 0.0765)]},
    "Wyoming": {"type": "flat", "rate": 0.0},
}

def f1_opt_tax_calculator(income, state, include_social_security, include_medicare, med_ins_biweekly):
    """
    Calculates estimated federal, state, Social Security, and Medicare taxes
    for an F1 OPT student (Indian national) with an option for a pre-tax medical insurance deduction.
    
    The medical insurance cost is entered as a biweekly amount, converted to annual,
    and then subtracted from the gross income. The effective income (gross income minus
    annual medical insurance) is then used for tax calculations.
    """
    # Convert biweekly medical insurance to an annual amount
    annual_med_insurance = med_ins_biweekly * 26
    
    # Effective income after deducting medical insurance
    effective_income = income - annual_med_insurance
    
    # Standard Deduction for Indian F1 OPT Students (2024)
    STANDARD_DEDUCTION = 14600
    taxable_income = max(0, effective_income - STANDARD_DEDUCTION)
    
    # Federal Tax Calculation (2024 brackets for single filers)
    federal_brackets = [
        (0, 11600, 0.10),
        (11600, 47150, 0.12),
        (47150, 100525, 0.22),
        (100525, 191950, 0.24),
        (191950, 243725, 0.32),
        (243725, 609350, 0.35),
        (609350, float('inf'), 0.37)
    ]
    federal_tax = 0
    for lower, upper, rate in federal_brackets:
        if taxable_income > lower:
            taxed_amount = min(taxable_income, upper) - lower
            federal_tax += taxed_amount * rate

    # State Tax Calculation using the state's tax brackets or flat rate
    state_info = STATE_TAX_INFO.get(state)
    if state_info is None:
        state_tax = taxable_income * 0.05
    elif state_info["type"] == "flat":
        state_tax = taxable_income * state_info["rate"]
    elif state_info["type"] == "brackets":
        state_tax = 0
        for lower, upper, rate in state_info["brackets"]:
            if taxable_income > lower:
                taxed_amount = min(taxable_income, upper) - lower
                state_tax += taxed_amount * rate

    # Social Security Tax Calculation on effective income
    if include_social_security:
        SOCIAL_SECURITY_RATE = 0.062
        WAGE_BASE_LIMIT = 160200  # Wage base limit for Social Security tax
        ss_income = effective_income
        social_security_tax = (WAGE_BASE_LIMIT * SOCIAL_SECURITY_RATE) if ss_income > WAGE_BASE_LIMIT else ss_income * SOCIAL_SECURITY_RATE
    else:
        social_security_tax = 0

    # Medicare Tax Calculation on effective income
    if include_medicare:
        MEDICARE_RATE = 0.0145
        ADDITIONAL_MEDICARE_RATE = 0.009  # Additional 0.9% for income above threshold
        MEDICARE_THRESHOLD = 200000
        med_income = effective_income
        if med_income <= MEDICARE_THRESHOLD:
            medicare_tax = med_income * MEDICARE_RATE
        else:
            medicare_tax = (MEDICARE_THRESHOLD * MEDICARE_RATE +
                            (med_income - MEDICARE_THRESHOLD) * (MEDICARE_RATE + ADDITIONAL_MEDICARE_RATE))
    else:
        medicare_tax = 0

    total_tax = federal_tax + state_tax + social_security_tax + medicare_tax
    effective_tax_rate = (total_tax / income) * 100 if income > 0 else 0

    # Net income is effective income after taxes
    net_income = effective_income - total_tax

    # Prepare annual results
    results_annual = {
        "Gross Income": income,
        "Annual Medical Insurance Deduction": annual_med_insurance,
        "Effective Income (Gross - Insurance)": effective_income,
        "Taxable Income": taxable_income,
        "Federal Tax": round(federal_tax, 2),
        "State Tax": round(state_tax, 2),
        "Social Security Tax": round(social_security_tax, 2),
        "Medicare Tax": round(medicare_tax, 2),
        "Total Tax": round(total_tax, 2),
        "Net Income (Effective Income - Taxes)": round(net_income, 2),
        "Effective Tax Rate (%)": round(effective_tax_rate, 2)
    }

    # Convert annual amounts to biweekly amounts (26 pay periods)
    def biweekly(amount):
        return round(amount / 26, 2)
    
    results_biweekly = { key: biweekly(value) for key, value in results_annual.items() if isinstance(value, (int, float)) }

    return results_annual, results_biweekly

# Streamlit UI
st.title("F1 OPT Tax Calculator")

income = st.number_input("Enter your annual income ($):", min_value=0, value=75000)
state = st.selectbox("Select your state:", sorted(STATE_TAX_INFO.keys()))

include_social_security = st.checkbox("Include Social Security Tax?", value=True)
include_medicare = st.checkbox("Include Medicare Tax?", value=True)

med_ins_biweekly = st.number_input("Enter your biweekly Medical Insurance cost ($):", min_value=0.0, value=0.0, step=0.1)

if st.button("Calculate Tax"):
    annual_results, biweekly_results = f1_opt_tax_calculator(income, state, include_social_security, include_medicare, med_ins_biweekly)
    st.write("### Annual Tax Breakdown")
    st.write(annual_results)
    st.write("### Biweekly Pay Breakdown")
    st.write(biweekly_results)
