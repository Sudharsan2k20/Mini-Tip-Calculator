print("Welcome to the tip calculator")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15"))
actual_tip = tip/100
total_tip_amount = bill * actual_tip
total_amount=bill + total_tip_amount
split = int(input("Hpw many people to split the bill?"))
pay = round(total_amount/split , 2)
print(f"Each person should pay {pay}")
