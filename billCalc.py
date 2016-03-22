print("Electricity Bill Estimator")

Cost = float(input("Enter cents per kWh: "))
Usage = float(input("Enter daily use in kWh: "))
Period = float(input("Enter number of billing days: "))

Bill = (Cost*Usage*Period)/100

print("Estimated Bill: $", Bill)