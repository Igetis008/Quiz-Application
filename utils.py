def get_valid_choice(prompt, valid_options):
    """Get a valid choice from the user"""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_valid_number(prompt, min_val=1, max_val=None):
    """Get a valid number from the user within a range"""
    while True:
        try:
            num = int(input(prompt))
            if max_val:
                if min_val <= num <= max_val:
                    return num
                else:
                    print(f"Please enter a number between {min_val} and {max_val}.")
            else:
                if num >= min_val:
                    return num
                else:
                    print(f"Please enter a number greater than or equal to {min_val}.")
        except ValueError:
            print("Please enter a valid number.")

def confirm_action(prompt):
    """Get confirmation from the user (Yes/No)"""
    while True:
        choice = input(f"{prompt} (Y/N): ").strip().upper()
        if choice in ["Y", "YES"]:
            return True
        elif choice in ["N", "NO"]:
            return False
        else:
            print("Please enter Y (Yes) or N (No).")