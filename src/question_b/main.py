#add import

import question_b

def main():
    while True:
        try:
            day_number = int(input("Enter a number (1 through 7): "))
            day_of_week = question_b.get_day_of_week(day_number)
            print("Day of the week:", day_of_week)
        except ValueError:
            print("Error: Please enter a valid number.")
        
        choice = input("Do you want to try again? (yes/no): ").lower()
        if choice not in ('yes', 'y'):
            break

main()