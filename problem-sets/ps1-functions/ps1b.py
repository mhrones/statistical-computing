#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: flaherty
"""

def compute_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
    """Compute the number of months needed to save."""

    # TODO: Implement me

    # Integer to keep track of how many months have passed
    month_counter = 0

    # Defines current amount saved, and how
    # much is needed for the down payment
    current_savings = 0
    portion_down_payment = 0.25 * total_cost

    # (1) Finding total monthly salary, and how much
    # is getting saved per month
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary*portion_saved

    # Finding monthly investment return rate
    r_yearly = 0.04
    r_monthly = r_yearly/12

    # Keeping track of time until next raise
    months_till_raise = 0


    # Continuing until our savings is greater
    # than or equal to down payment amount
    while current_savings < portion_down_payment:
        #print("Current Month: ", month_counter )
        # Checking if it's time for a raise!
        if(months_till_raise == 6):
            #print("Raise Time!")

            # Re-defining variables in (1) to account for the raise
            dollars_raise = annual_salary * semi_annual_raise
            annual_salary = annual_salary + dollars_raise
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary*portion_saved
            months_till_raise = 0
            #print("New Salary: ", annual_salary)


        # Adding investment profits to our current_savings
        current_savings += current_savings * r_monthly
        # Adding salary saved to our current_savings
        current_savings += monthly_savings
        # One month has passed
        month_counter += 1
        months_till_raise += 1

    return month_counter


if __name__ == "__main__":
    annual_salary = int(input("Enter your starting annual salary: "))
    # TODO: Implement me
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of the house: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    num_months = compute_months(annual_salary, portion_saved, total_cost, semi_annual_raise)
    print("Number of months: %d" % num_months)
