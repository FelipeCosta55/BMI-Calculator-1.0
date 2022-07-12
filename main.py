height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# By default, the input comes as string, so we need to change it to float type in order to calculate correctly. 
height_float = float(height)
weight_float = float(weight)

# Create the bmi variable, make the calculation ant print its result.
bmi = weight_float / (height_float ** 2)
print(int(bmi))