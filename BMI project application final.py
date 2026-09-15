# This is a BMI system it helps the user to navigate through the system and calculate their BMI, ideal weight and also give them a personalized calorie recommendation based on their fitness goals
# First we will define all the functions to have our own personal library of functions that we can call later in the main execution loop
def calculate_bmi_metric(weight_kg, height_m):
    """Calculates BMI using standard metric units."""
    return weight_kg / (height_m ** 2)

def calculate_ideal_weight_metric(height_m):
    """Calculates healthy target weight based on the metric median parameter (21.7)."""
    return 21.7 * (height_m ** 2)

def convert_imperial_to_metric(feet, inches, weight_lbs):
    """Converts feet, inches, and pounds into meters, cm, and kg."""
    total_inches = (feet * 12) + inches
    height_cm = total_inches * 2.54
    height_m = height_cm / 100
    weight_kg = weight_lbs * 0.453592
    return total_inches, height_m, height_cm, weight_kg

def determine_bmi_category(bmi):
    """Classifies the BMI score into standard health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight_kg, height_cm, age, gender):
    """Calculates Basal Metabolic Rate using streamlined Mifflin-St Jeor logic."""
    if gender == "Male":
        adjustment = 5
    else:
        adjustment = -161
    return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + adjustment

def get_goal_adjustments(goal_choice, base_calories):
    """Adjusts baseline calories and provides guidance based on goal choice."""
    if goal_choice == "1":    # Gain Weight
        final_calories = int(base_calories + 400)
        advice = "Advice: Focus on a calorie surplus with nutrient-dense foods and progressive strength training."
    elif goal_choice == "2":  # Lose Weight
        final_calories = int(base_calories - 400)
        advice = "Advice: Create a safe calorie deficit by eating high-protein, high-fiber foods, and increasing cardio."
    else:                     # Maintain / Fit
        final_calories = int(base_calories)
        advice = "Advice: Maintain your balanced diet, combine strength training with cardio, and stay hydrated."
    return final_calories, advice

# Now the application itself will start, and we will use a while loop to automatically run the code until the user decides to stop
print("Welcome to Aurahealth! your health assistant and BMI calculator)")

running = True
while running:
    # STEP 1: The user enters needed data (weight, height, age, gender)
    name = input("\nEnter your name: ")
    
    print("Select your gender:")
    print("1.Male")
    print("2.Female")
    gender_choice = input("Choice (1 or 2): ").strip()
    gender = "Male" if gender_choice == "1" else "Female"
    
    age = int(input("Enter your age: "))
    
    print("\nChoose your measurement system:")
    print("1.Metric (kg / meters)")
    print("2.Imperial (pounds / feet & inches)")
    unit_choice = input("Choice (1 or 2): ").strip()
    
    # STEP 2: Measurements and calculations
    if unit_choice == "1":
        weight = float(input("Enter weight in kg (example, 70): "))
        height = float(input("Enter height in meters (example, 1.75): "))
        bmi = calculate_bmi_metric(weight, height)
        ideal_weight = calculate_ideal_weight_metric(height)
        
        w_kg = weight
        height_cm = height * 100  
        weight_unit = "kg"
        
    else:
        weight = float(input("Enter weight in pounds (example, 150): "))
        feet, inches = map(int, input("Enter height (example, 5 11 for 5ft 11in): ").split())
        total_inches, height, height_cm, w_kg = convert_imperial_to_metric(feet, inches, weight)
        
        bmi = (weight / (total_inches ** 2)) * 703
        ideal_weight = (21.7 * (total_inches ** 2)) / 703
        weight_unit = "lbs"
        
    # STEP 3: Determine the BMI category
    category = determine_bmi_category(bmi)
    
    # STEP 4: Print out the health summary (Before goals)
    print(f"\nHEALTH SUMMARY FOR {name.upper()}")
    print(f"•Demographics: {age} years old | {gender}")
    print(f"•BMI: {round(bmi, 2)}")
    print(f"•Status: {category}")
    print(f"•Your Ideal Healthy Weight is approximately: {round(ideal_weight, 1)} {weight_unit}")
        
    # STEP 5: The goal selection and calorie calculator
    print("\nSelect your current fitness goal:")
    print("1.Gain Weight")
    print("2.Lose Weight")
    print("3.Maintain / Be More Fit")
    goal_choice = input("Choice (1, 2, or 3): ").strip()
    
    # Calculate BMR, scale for activity levels, and compute goal values via functions
    bmr_calories = calculate_bmr(w_kg, height_cm, age, gender)
    tdee_calories = bmr_calories * 1.2  # Sedentary baseline activity multiplier
    final_calories, advice = get_goal_adjustments(goal_choice, tdee_calories)
    
    # STEP 6: Nutritional advice and final output
    print(f"\nRecommended Daily Calorie Intake: {final_calories} kcal / day")
    print(f"{advice}")
    
    # STEP 7: The loop control to allow the user to restart or exit the program
    repeat = input("\nWould you like to calculate for a family member, friend, or restart? (yes / no): ").strip().lower()
    if repeat != "yes":
        running = False  # Tells the engine to stop the loop

print("\nThank you for using Aurahealth! Good luck with your goals!")