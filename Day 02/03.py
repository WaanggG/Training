weigh = input("Enter your weigh in kg ")
height = input("Enter your height in m ")

weigh_as_int = int(weigh)
height_as_float = float(height)

bmi = weigh_as_int / height_as_float**2
bmi_as_int = int(bmi)
print(bmi_as_int)


