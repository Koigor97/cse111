# Inorder for me to get accuracy in calculation I need to use the math-module,
# to use the math.pi function. Also using the datetime module to get today's date.
import math
from datetime import datetime

print("""""""""""""""""""       Welcome Astro Wheel and Tires       """"""""""""""""""")
print("Enter the specification for the Tire you want.\n")

tire_width = float(input("Enter the width of the tire in millimeters(mm): "))
tire_aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
tire_diameter = float(input("Enter the diameter of the tire: "))
print()


def volume_formula(width, aspect_ratio, diameter) -> float:
    """This function calculates the width, aspect-ratio, and diameter of the rim
    and returns a value as the volume of space inside the tire."""
    the_volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
    return the_volume


result = volume_formula(tire_width, tire_aspect_ratio, tire_diameter)

if tire_width in range(100, 256) and tire_aspect_ratio in range(50, 86) and tire_diameter in range(15, 26):
    print(f"The approximate volume inside the tire would be: {result:.2f} liters.\n"
          f"The price for the Tire is $299.99\n")
    is_interested = input("Do you want proceed with the purchase? ").lower()

    if is_interested == "yes":
        cell_num = int(input("\nEnter your telephone number (make sure you include your country-code): "))
        print("Your purchase was successful✅!")
        data_and_time = datetime.now()

        with open("volume.txt", "at") as data_file:
            data_file.write(f"{data_and_time:%Y-%m-%d} | {tire_width}, {tire_aspect_ratio},"
                            f" {tire_diameter}, {result:.2f} | {cell_num}\n")
    else:
        print("\nThank you for choosing our services. Come back soon✌️")

else:
    print("Oops. Sorry, the tire specification you entered is out of stock")

view_data = input("\nWould you like to view the data-file? (Yes/No): ").lower()
if view_data == "yes":
    print()
    with open("volume.txt", "r") as data_file:
        data = data_file.read()
        print(data)
else:
    print("\nThank you for choosing our services. Come back soon✌️")
