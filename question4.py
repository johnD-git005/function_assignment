''' Write a function triangle_area(base, height) that calculates the area of a triangle using the formula:
Area=1/2×base×height
Example: triangle_area(10, 5) → 25.0 '''

base = float(input("Base Of Triangle: "))
height = float(input("Height of Triangle: "))

def triangle_area():

	result = 1/2 * base * height
	print(f"Area →  {result}")

triangle_area()
