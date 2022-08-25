print("Welcome to the tip calculator!")

bill = float(input("What was the total bill $ "))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_persion = total_bill / people
final_amount = round(bill_per_persion, 2)

print(f"Each persion should pay {final_amount} $ ")
