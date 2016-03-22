print("Electricity Bill Estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

Tariff = int(input("Which Tariff? 11 or 31: "))
if Tariff == 11:
    Tariff = TARIFF_11
elif Tariff == 31:
    Tariff = TARIFF_31
else:
    print("Unavailable option.")
Usage = float(input("Enter daily use in kWh: "))
Period = float(input("Enter number of billing days: "))

Bill = float(Tariff)*Usage*Period

print("Estimated Bill: $", round(Bill, 2))