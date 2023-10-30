
# Now I'm going to try to make my credit card function
print("Hello! Which card is best for you? Let's gather some data.\n"
      " Please input how much money you spend per MONTH in the following categories:")
Total_Spend = input("Total Spend (per month)= ")
Travel = int(input("Monthly Travel Spend = "))
Dining = int(input("Monthly Dining Spend = "))
Gas = int(input("Monthly Gas Spend = "))
Bills_Utilities = int(input("Monthly Bills and Utilities Spend = "))
Education = int(input("Monthly Education Spend = "))
Entertainment = int(input("Monthly Entertainment Spend = "))
Personal = int(input("Monthly Personal Spend = "))
Home = int(input("Monthly Home Spend = "))
Groceries = int(input("Monthly Groceries Spend = "))
The_rest = int(Gas + Bills_Utilities + Education + Entertainment + Personal + Home)


print("\nOkay. So you spend " + str(Total_Spend) + " dollars per month total. " + str(Travel) + " on travel, ")
print(str(Dining) + " on dining, " + str(Gas) + " on gas, and " + str(Groceries) + " on groceries. ")


# important variables for CSP here
csp_travel_credit = 50
csp_annual_fee = 95
csp_rewards_multiplier = 1.25
csp_annual_adjusted_fee = 45
csp_monthly_rewards = (csp_rewards_multiplier * int((Travel * .02) + (Dining * .03) + (The_rest * .01) - (csp_annual_adjusted_fee / 12)))

# important variables for CSR here
csr_travel_credit = 300
csr_annual_fee = 550
csr_rewards_multiplier = 1.5
csr_annual_adjusted_fee = 250
csr_additional_user_fee = 75
csr_monthly_rewards = (csr_rewards_multiplier * int((Travel + Dining) * .03 + (The_rest * .01))) - (csr_annual_adjusted_fee / 12)



# printing my results

if csp_monthly_rewards > csr_monthly_rewards:
    print("\nYou should go with the Chas Sapphire Preferred. Your monthly rewards will be " + str(csp_monthly_rewards))
    print("\nWhereas with the Chase Sapphire reserve, your monthly rewards would be " + str(csr_monthly_rewards))
    print("\nYour annual rewards would be " + str(csp_monthly_rewards * 12))
else:
   print("\nYou should go with the Chase Sapphire Reserve, as your monthly rewards will be $" + str(csr_monthly_rewards))
   print("\nWhereas with the Chase Sapphire preferred, your monthly rewards would be $" + str(csp_monthly_rewards))
   print("\nYour annual rewards would be $" + str(csr_monthly_rewards * 12))