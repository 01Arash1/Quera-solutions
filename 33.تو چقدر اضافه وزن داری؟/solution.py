Weight = float(input())
Height = float(input())

bmi = Weight/(Height**2)

if bmi < 18.5:
    stats = "Underweight"
elif 18.5 <= bmi < 25:
    stats = "Normal"
elif 25 <= bmi < 30:
    stats = "Overweight"
else:
    stats = "Obese"

print(f"{bmi:1.2f}\n{stats}")