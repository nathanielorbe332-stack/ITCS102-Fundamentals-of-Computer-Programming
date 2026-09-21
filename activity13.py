print("=============================================================================")
age = int(input("\t\tPlease enter your age: "))
is_employed = bool(input("\t\tAre you employed? (yes/no): ").lower() == "yes")
credit_score = eval(input("\t\tPlease enter your credit score: "))
annual_income = eval(input("\t\tPlease enter your annual income: "))
has_collateral = bool(input("\t\tDo you have collateral? (yes/no): ").lower() == "yes")
print("=============================================================================")
if age >= 21 and is_employed == True:
    print("Approved: Meets baseline criteria")

    if credit_score >= 750:
        print("Approved: Excellent credit score")
        if annual_income >= 100000:
            print("Approved: Sufficient annual income")
            base_interest_rate = 4.5
            print("hello, your base interest rate is: ", base_interest_rate, "%")
        else:
            base_interest_rate = 5.0
            print("hello, your base interest rate is: ", base_interest_rate, "%")

    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True: 
            base_interest_rate = 7.0
            print("hello, your base interest rate is: ", base_interest_rate, "%")
        elif annual_income < 40000:
            base_interest_rate = 9.5
            print("hello, your base interest rate is: ", base_interest_rate, "%")
        else:
            base_interest_rate = 8.0
            print("hello, your base interest rate is: ", base_interest_rate, "%")
else:
    print("Rejected: Fails baseline criteria")

    if credit_score < 600:
        print("Rejected: Poor credit score")
print("=============================================================================")
