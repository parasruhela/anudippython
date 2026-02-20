
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income (₹): "))
existing_loan = float(input("Enter existing loan amount (₹): "))


if credit_score < 600:
    print("Loan Rejected: Credit score too low.")
elif 600 <= credit_score < 750:
    
    if monthly_income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loans.")
    else:
        print("Loan Under Review: Meets credit score criteria, further verification required.")
elif credit_score >= 750:
    print("Loan Approved: Excellent credit score.")
