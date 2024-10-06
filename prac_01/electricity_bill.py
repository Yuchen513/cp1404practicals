"Electricity bill estimator"

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff_choice == "11":
    rate = TARIFF_11
elif tariff_choice == "31":
    rate = TARIFF_31
else:
    print("Invalid tariff choice.")
    exit()
estimated_bill = rate * daily_use * billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")