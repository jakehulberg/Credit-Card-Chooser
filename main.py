
# Now I'm going to try to make my credit card function
print("Hello! Which card is best for you? Let's gather some data.\n"
      " Please input how much money you spend per MONTH in the following categories:")
Total_Spend = input("Total Spend (per month)= ")
Travel = int(input("Monthly Travel Spend = "))
Dining = int(input("Monthly Dining Spend = "))
Gas = int(input("Monthly Gas Spend = "))
Groceries = int(input("Monthly Groceries Spend = "))

print("\nOkay. So you spend " + str(Total_Spend) + " dollars per month total. " + str(Travel) + " on travel, ")
print(str(Dining) + " on dining, " + str(Gas) + " on gas, and " + str(Groceries) + " on groceries. ")

csp_rewards = int((Travel * .03) + (Dining * .03) + (Gas * .01) + (Groceries * .01))
csr_rewards = int(((Travel + Dining) * .04) + ((Gas + Groceries) * .10))

if csp_rewards > csr_rewards:
    print("\nWhereas with the Chase Sapphire reserve, your monthly rewards would be " + str(csr_rewards))
else:
   print("\nYou should go with the Chase Sapphire Reserve, as your monthly rewards will be $" + str(csr_rewards))
   print("\nWhereas with the Chase Sapphire preferred, your monthly rewards would be $" + str(csp_rewards))
