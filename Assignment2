def calculate_bmi(weight, height):
    return weight / (height ** 2)

def health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

while True:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = calculate_bmi(weight, height)
    status = health_status(bmi)
    
    print(f"BMI: {bmi:.2f} - {status}")
    
    again = input("Calculate again? (y/n): ")
    if again.lower() != 'y':
        break
