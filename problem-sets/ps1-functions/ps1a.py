#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mhrones
"""

def compute_months(annual_salary, portion_saved, total_cost):
    """Compute the number of months needed to save."""

    # Integer to keep track of how many months have passed
    month_counter = 0

    # Defines current amount saved, and how
    # much is needed for the down payment
    current_savings = 0
    portion_down_payment = 0.25 * total_cost

    # Finding total monthly salary, and how much
    # is getting saved per month
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary*portion_saved

    # Finding monthly investment return rate
    r_yearly = 0.04
    r_monthly = r_yearly/12


    # Continuing until our savings is greater
    # than or equal to down payment amount
    while current_savings < portion_down_payment:

        # Adding investment profits to our current_savings
        current_savings += current_savings * r_monthly
        # Adding salary saved to our current_savings
        current_savings += monthly_savings
        # One month has passed!
        month_counter += 1



    # TODO: Implement me
    return month_counter


if __name__ == "__main__":
    annual_salary = int(input("Enter your starting annual salary: "))
    # TODO: Implement me

    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of the house: "))



    num_months = compute_months(annual_salary, portion_saved, total_cost)
    print("Number of months: %d" % num_months)
