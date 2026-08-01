print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

per_person = (bill/people)*((100+tip)/100)
rounded_per_person = round(per_person,2)
print(f"Each person should pay: {rounded_per_person}")
