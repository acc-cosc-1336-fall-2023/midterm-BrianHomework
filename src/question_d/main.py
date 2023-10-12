#add import

from question_d import get_assessment_value, get_tax_assessed

# Main program

while True:
    user_input = input("Enter the actual value of the property (or 'q' to quit): ").strip().lower()

    if user_input == 'q' or user_input == 'quit':
        break  # Exit the loop if the user enters 'q' or 'quit'

    try:
        actual_value = float(user_input)
        assessment_value = get_assessment_value(actual_value)
        property_tax = get_tax_assessed(assessment_value)

        print(f"Assessment Value: ${assessment_value:.2f}")
        print(f"Property Tax: ${property_tax:.2f}")
    except ValueError:
        print("Please enter a valid numeric value for the property's actual value.")