from datetime import datetime
from typing import Union




def main():
    """This function prompt the user for the necessary inputs, calls the required functions,
     and display the values to user."""

    name = input("What is your Name: ").lower()
    gender = input("Please enter your Gender (M/F): ").lower()
    d_o_b = input("Enter your Date Of Birth in this format (YYYY-MM-DD); ")
    weight = float(input("Enter your Weight in U.S pounds (lbs): "))
    height = input("Enter your Height in U.S feet.inches in this format (ft.inch): ").split(".")

    age = compute_age(d_o_b)
    the_weight = lbs_to_kg(weight)
    the_height = inch_to_meter(height)
    bmi = body_mass_index(the_weight, the_height)
    height_to_cm = the_height * 100
    bmr = basal_metabolic_rate(gender, age, the_weight, height_to_cm)

    print()
    print(f"Your age: {age}")
    print(f"Your weight (kg): {the_weight}")
    print(f"Your height (in meters): {the_height:.3f}")
    print(bmi)
    print(bmr)


def compute_age(birthdate: str) -> int:
    """This function compute and return a person's age in years."""
    birthday = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthday.year

    if today.month < birthday.month:
        years -= 1

    return years


def lbs_to_kg(weight: float) -> float:
    """This function converts and returns the weight from pounds (lbs)
     to kilogram."""
    to_kg = round(weight * 0.45359237, 2)
    return to_kg


def inch_to_meter(height: list) -> float:
    """This function convert and returns the height from feet. Inches (ft.in)
    to metes (m)"""
    to_inches = int(height[0]) * 12 + int(height[1])
    to_centimeter = to_inches * 2.54
    to_meters = to_centimeter / 100
    return to_meters


def body_mass_index(weight: float, height: float) -> str:
    """This function calculates and returns a value of the BMI of a person and
    their health status"""
    bmi = round(weight / height ** 2, 2)

    if (bmi >= 15.0) and (bmi < 18.5):
        return f"Your BMI is {bmi}, you are Underweight."
    elif (bmi >= 18.6) and (bmi < 25.5):
        return f"Your BMI is {bmi}, you are Normal weight."
    elif (bmi >= 25.5) and (bmi < 30.5):
        return f"Your BMI is {bmi}, you are Overweight."
    elif bmi >= 30.5:
        return f"Your BMI is {bmi}, you are Obese."


def basal_metabolic_rate(gender: str, age: int, weight: float, height: float) -> Union[str, int, float]:
    """This function compute and return the BMR value of a person"""
    if gender == "f":
        bmr = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
        return f"Your BMR is {bmr} calories per day."
    else:
        bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
        return f"Your BMR is {bmr} calories per day"


main()
