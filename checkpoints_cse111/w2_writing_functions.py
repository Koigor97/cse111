

def main():
    """This function prompts the user for the first and second odometer reading, with the amount of gallons.
    Calls the miles_per_gallon and lp100k_from_mpg functions, stores their values, and display it for the user """
    start_odometer = float(input("Enter the first odometer reading (miles): "))
    end_odometer = float(input("Enter the second odometer reading (miles): "))
    gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(start_odometer, end_odometer, gallons)
    lp_100k = lp100k_from_mpg(mpg)

    print(f"{round(mpg, 1)} miles per gallon\n{lp_100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start: float, end: float, gallons: float) -> float:
    """This function compute and return the value,  the average number of 'miles'
    that a vehicle traveled per gallon of fuel."""
    calc = abs(end - start) / gallons
    return calc


def lp100k_from_mpg(mpg: float) -> float:
    """This function converts and return the value from mile to liters per 100 kilometer"""
    l_per_100k = 235.215 / mpg
    return l_per_100k


main()
