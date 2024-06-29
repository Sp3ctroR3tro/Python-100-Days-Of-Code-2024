TAX = 0.06
# Prompt for what the total bill and the party size:
bill = float(input("What is the current bill total?\n$"))
party = int(input("What is the size of our party?\n"))

# Determining tip values
tip_amount = float(input("Enter the tip percentage:\n"))

# Calculating the total bill including tax and tip
total_before_tip = float(bill * (1 + TAX))
total_tip = float(total_before_tip * (tip_amount / 100))
total_bill = total_before_tip + total_tip
# Calculating how much each person would have to pay
per_person_total = float(total_bill / party)

# Displaying output
print(f"Each person will need to pay ${per_person_total:.2f}")
