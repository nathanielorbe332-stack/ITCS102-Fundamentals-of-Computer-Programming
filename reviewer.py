#reviewerninat

owner_age = int(input("Enter your age: "))
rev = float(input("Enter your monthly revenue: "))
c_s = int(input("Enter your credit score: "))
yrs_b = float(input("Years in business: "))
has_defaults = bool(input("have you filed for bankruptcy: "))
collateral = input("What is your collateral: ")
c_value = float(input("Value your collateral: "))

max_loan = 0 
base_fee = 0.0

if owner_age >= 21 and yrs_b >= 2.0 and has_defaults == False:
    print("Baseline requirement pass!")
    print("Never filed bankcruptcy")
    
    if c_s >= 720:
        max_loan = rev * 3  
        print("max loan for high credit score is ", max_loan)
        print("your credit score is high!")
        
        if rev >= 50000:
            base_fee = max_loan * 0.015
            print("your base fee rate is ", base_fee)
        else: 
            base_fee = max_loan * 0.025
            print("insufficient credit score!", base_fee)
        
        if c_value >= max_loan:
            print("Collateral", collateral, "Eligible!")   
        else:
            print("REJECTED: insufficient collateral value")
        
            surcharge = max_loan * base_fee
        if c_value % 5000 != 0:
            surcharge += 250
            
    elif c_s <= 620 and c_s < 720:
        max_loan = rev * 1.5
        print("max loan is ", max_loan)
        if yrs_b >= 5.0:
            base_fee = max_loan * 0.2
            print("you base fee rate is", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("your base fee is not eligible ", base_fee)
       
        if c_value >= max_loan:
            print("Collateral Eligible!")   
        else:
            print("REJECTED: insufficient collateral value")
    elif c_s < 620:
        print("Rejected: Credit score below requirements")
    else:
        print("not tier 1")
else:
    print("Rejected: High risk Application")
