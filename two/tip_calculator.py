print("Hello, welcome to your tip calculator.\n")
initial_bill = float(input("What was the total bill? GHc\n"))
percentage_tip = int(input("What percentage tip would you like to give? eg. 10, 12, 15\n"))
number_of_people = int(input("How many people are splitting the bill?\n"))

semi_final_bill = initial_bill + (( percentage_tip / 100 ) * initial_bill)
final_bill = round((semi_final_bill / number_of_people), 2)

print(f"Each person should pay GHc{final_bill}.")
