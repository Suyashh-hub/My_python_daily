def calculate_bill():
    customer_no = input("Enter Customer Number: ")
    units = float(input("Enter Power Consumed (units): "))
    
    if units <= 100:
        amount = units * 1
    elif units <= 300:
        amount = 100 + (units - 100) * 1.25
    elif units <= 500:
        amount = 350 + (units - 300) * 1.50
    else:
        amount = 650 + (units - 500) * 1.75

    print("-" * 30)
    print(f"      ELECTRICITY BILL")
    print("-" * 30)
    print(f"Customer No    : {customer_no}")
    print(f"Units Consumed : {units}")
    print(f"Total Amount   : Rs. {amount:.2f}")
    print("-" * 30)

calculate_bill()
