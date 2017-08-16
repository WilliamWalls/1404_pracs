"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter your sales: $"))
if sales < 0:
    print("Invalid Sales")
while sales >= 0:
    if sales >= 1000:
        print("Your bonus is: ${}".format(sales * 1.5 / 10))
    elif print("Your bonus is: ${}".format(sales * .1)):
        if sales == 1000:
            print("Your bonus is:$150")
    sales = float(input("Enter your sales: $"))




