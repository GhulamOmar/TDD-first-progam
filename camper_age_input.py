"""
Program: camper_age_input.py
Author: Ghulam Omar
Last date modified: 09/07/19
This program converts age in years to months.
The input is an integer representing the age in years.
The output an integer representing the age in months.
"""


def convert_to_months(age_in_years, age_in_months):  # Function definition.

    return age_in_years*age_in_months # return statement.


if __name__ == '__main__':
    age_in_years = int(input("Enter your age "))  # prompt the user/accepts user input
    age_in_months = 12 # variable declaration.
    answer = age_in_years*age_in_months # calculation.
    print(age_in_years,"years is", answer, "months")  # output the result.
