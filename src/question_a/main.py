#add import

import question_a

def main():
    while True:
        user_input = input("Enter a string (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break

        if not user_input.replace(" ", "").isalpha():
            print("I don't like numbers, only words please and thank you")
        else:
            reversed_result = question_a.reverse_string(user_input)
            print("Reversed:", reversed_result)
main()