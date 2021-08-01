#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: flaherty
"""

def compute_rate(annual_salary):
    """Compute the savings rate needed"""



    # TODO: Implement me

    # Setting asssumptions from PS1 PDF

    # Setting a variable to the orignal input
    input_annual_salary = annual_salary

    semi_annual_raise = 0.07

    # Calculating investment rates
    r_yearly = 0.04
    r_monthly = r_yearly/12

    # Calculating needed down payment
    total_cost = 1000000
    down_payment = 0.25*total_cost

    # Constructing the original guess, as a integer between 0 and 10,000
    min = 0
    max = 10000
    guess_int = min+max/2
    bisection_count = 0

    possibl = True

    cont = True
    while cont is True:

        # Here's to another bisection!
        bisection_count += 1

        # Resetting variables
        annual_sal = input_annual_salary
        monthly_salary = annual_sal/12

        # Calculating monthly savings based on the new guess
        guess_deci = guess_int/10000
        monthly_savings = monthly_salary * guess_deci
        current_savings = 0

        # Setting up month counts and raise logic
        month_counter = 0
        months_till_raise = 0

        while month_counter < 36:


            # Checking if it's time for a raise!
            if(months_till_raise == 6):

                # Re-defining variables in (1) to account for the raise
                dollars_raise = annual_sal * semi_annual_raise
                annual_sal = annual_sal + dollars_raise
                monthly_salary = annual_sal / 12
                monthly_savings = monthly_salary*guess_deci
                months_till_raise = 0


            # Adding investment profits to our current_savings
            current_savings += current_savings * r_monthly
            # Adding salary saved to our current_savings
            current_savings += monthly_savings
            # One month has passed
            month_counter += 1
            months_till_raise += 1


        # Checking to see if the amount saved falls within the needed amount
        if abs(current_savings - down_payment) < 100:
            cont = False
            #break

        # If it is greater, then we set our new
        # maximum equal to our current guess
        if current_savings > down_payment:
            max = guess_int
        else:
        # Otherwise, we set out new minimum equal to our current guess
            min = guess_int

        # If we ever get to a point where the min is greater than the max,
        # it's not possible to save that amount in 36 months!
        if min >= max:
            possibl = False
            cont = False
            #break

        # making a new guess, based on the middle of the new min and max
        guess_int = (max + min) / 2

    # Converting our final guess to a decimal
    guess_deci = guess_int/10000

    # Setting rate equal to the final guess
    rate = guess_deci
    # If the loop found it wasn't possible, we reset rate to 'None'
    if possibl == False:
        rate = None
        bisection_count = None


    return rate, bisection_count



if __name__ == "__main__":
    annual_salary = int(input("Enter your starting annual salary: "))

    rate, bisection_count = compute_rate(annual_salary)
    if rate is None:
        print("It is not possible to pay the down payment in three years.")
    else:
        print("Minimal savings rate: %f" % rate)
        print("Steps in bisection search: %d" % bisection_count)
