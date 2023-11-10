
# Credit card function using monthly numbers
def monthly_inputs ():
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

## Going to try a different list organization here for my categories

# categories = ["Travel", "Dining", "Gas", "Bills_Utilities", "Education", "Entertainment", "Personal",
#                   "Home", "Groceries"]
# spending_data = {}
# for category in categories:
#    spending_data[category] = float(input(f"Monthly {category} spend = $"))

#I don't understand how that will work in my code right now :(


    # important variables for CSP here
    csp_travel_credit = 50
    csp_annual_fee = 95
    csp_rewards_multiplier = 1.25
    csp_annual_adjusted_fee = 45
    csp_monthly_rewards = (csp_rewards_multiplier * int(
        (Travel * .02) + (Dining * .03) + (The_rest * .01) - (csp_annual_adjusted_fee / 12)))

    # important variables for CSR here

    csr_travel_credit = 300
    csr_annual_fee = 550
    csr_rewards_multiplier = 1.5
    csr_annual_adjusted_fee = 250
    auth_user_number = int(input("How many authorized users will you have? "))
    csr_additional_user_fee = (75 * auth_user_number)
    csr_monthly_rewards = (csr_rewards_multiplier * int((Travel + Dining) * .03 + (The_rest * .01))) - (
                csr_annual_adjusted_fee / 12) - (csr_additional_user_fee / 12)

    # printing my results

    if csp_monthly_rewards > csr_monthly_rewards:
        print("\nYou should go with the Chas Sapphire Preferred. Your monthly rewards will be " + str(
            csp_monthly_rewards))
        print("\nWhereas with the Chase Sapphire reserve, your monthly rewards would be " + str(csr_monthly_rewards))
        print("\nYour annual rewards would be " + str(csp_monthly_rewards * 12))
    else:
        print("\nYou should go with the Chase Sapphire Reserve, as your monthly rewards will be $" + str(
            csr_monthly_rewards))
        print("\nWhereas with the Chase Sapphire preferred, your monthly rewards would be $" + str(csp_monthly_rewards))
        print("\nYour annual rewards would be $" + str(csr_monthly_rewards * 12))


### Making the yearly inputs function
def yearly_inputs():
    print("Hello! Which card is best for you? Let's gather some data.\n"
          " Please input how much money you spend per YEAR in the following categories:")
    Total_Spend = input("Total Spend (per year)= ")
    Travel = int(input("Yearly Travel Spend = "))
    Dining = int(input("Yearly Dining Spend = "))
    Gas = int(input("Yearly Gas Spend = "))
    Bills_Utilities = int(input("Yearly Bills and Utilities Spend = "))
    Education = int(input("Yearly Education Spend = "))
    Entertainment = int(input("Yearly Entertainment Spend = "))
    Personal = int(input("Yearly Personal Spend = "))
    Home = int(input("Yearly Home Spend = "))
    Groceries = int(input("Yearly Groceries Spend = "))
    Shopping = int(input("Yearly Shopping Spend = "))
    The_rest = int(Gas + Bills_Utilities + Education + Entertainment + Personal + Home + Groceries + Shopping)

    print("\nOkay. So you spend " + str(Total_Spend) + " dollars per year total. " + str(Travel) + " on travel, ")
    print(str(Dining) + " on dining, " + str(The_rest) + " in the rest of the categories. ")

    # important variables for CSP here
    csp_travel_credit = 50
    csp_annual_fee = 95
    csp_rewards_multiplier = 1.25
    csp_annual_adjusted_fee = 45
    csp_yearly_rewards = (csp_rewards_multiplier * int(
        (Travel * 0.02) + (Dining * 0.03) + (The_rest * 0.01) - csp_annual_adjusted_fee))

    # important variables for CSR here

    csr_travel_credit = 300
    csr_annual_fee = 550
    csr_rewards_multiplier = 1.5
    csr_annual_adjusted_fee = 250
    auth_user_number = int(input("How many authorized users will you have? "))
    csr_additional_user_fee = auth_user_number * 75


    csr_yearly_rewards = (csr_rewards_multiplier * int((Travel + Dining) * 0.03 + (The_rest * 0.01)) -
            csr_annual_adjusted_fee - csr_additional_user_fee)

    # printing my results

    if csp_yearly_rewards >= csr_yearly_rewards:
        print("\nYou should go with the Chas Sapphire Preferred. Your yearly rewards will be " + str(
            csp_yearly_rewards))
        print("\nWhereas with the Chase Sapphire reserve, your yearly rewards would be " + str(csr_yearly_rewards))
    else:
        print("\nYou should go with the Chase Sapphire Reserve, as your yearly rewards will be $" + str(
            csr_yearly_rewards))
        print("\nWhereas with the Chase Sapphire preferred, your yearly rewards would be $" + str(csp_yearly_rewards))



### Which function should be called based off of users desired input


Monthly_vs_yearly = input("""We're going to help you decide between the Chase Sapphire Preferred and the Chase Sapphire Reserved based off
of your spending habits in different categories. Would you like to input monthly or yearly numbers? For Monthly, type M.
For yearly, type Y. """)

if Monthly_vs_yearly == "M":
    monthly_inputs()
else:
    yearly_inputs()



