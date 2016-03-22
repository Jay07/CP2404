print("Area Calculator")

width = float(input("Enter width: "))
height = float(input("Enter height: "))
depth = float(input("Enter depth: "))

area = width * height
volume = area * depth


print("Area: ", int(area), "Volume: ", int(volume))