import math

def calculate_diameter(horizontal, vertical):
    horizontal_diameter = 2 * math.sqrt((horizontal ** 2) / 4 + (vertical ** 2) / 4)
    vertical_diameter = 2 * math.sqrt((horizontal ** 2) / 4 + (vertical ** 2) / 4)
    return horizontal_diameter, vertical_diameter

horizontal = float(input("Enter the horizontal size of the tumor: "))
vertical = float(input("Enter the vertical size of the tumor: "))

horizontal_diameter, vertical_diameter = calculate_diameter(horizontal, vertical)

print("The horizontal diameter of the tumor is: {:.2f}".format(horizontal_diameter))
print("The vertical diameter of the tumor is: {:.2f}".format(vertical_diameter))
