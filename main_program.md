# Main Program Implementation

## Main Module (main.py)

Create a file named `main.py` with the following code:

```python
from database import create_connection, close_connection
from admin import admin_menu
from player import player_menu

def main():
    """Main program entry point"""
    print("="*60)
    print("WELCOME TO THE QUIZ SYSTEM")
    print("="*60)
    
    # Create database connection
    connection = create_connection()
    
    if not connection:
        print("Failed to connect to the database. Exiting...")
        return
    
    try:
        while True:
            print("\n" + "="*50)
            print("MAIN MENU")
            print("="*50)
            print("1. Admin Mode")
            print("2. Player Mode")
            print("3. Exit")
            print("-"*50)
            
            choice = input("Are you an Admin or a Player? (1-3): ").strip()
            
            if choice == "1":
                admin_menu(connection)
            elif choice == "2":
                player_menu(connection)
            elif choice == "3":
                print("Thank you for using the Quiz System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # Close database connection
        close_connection(connection)

if __name__ == "__main__":
    main()
```

## Utility Functions (utils.py)

Create a file named `utils.py` with utility functions for input validation:

```python
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
```

## Program Flow

1. **Program Start**: Welcome message is displayed
2. **Database Connection**: Establish connection to MySQL database
3. **Main Menu**: User chooses between Admin Mode, Player Mode, or Exit
4. **Admin Mode**: 
   - User can add new questions or view all questions
   - Returns to main menu after exiting admin mode
5. **Player Mode**:
   - User selects a category
   - Quiz is conducted with 5 random questions
   - Score is displayed at the end
   - Returns to main menu after quiz completion
6. **Exit**: Program terminates and database connection is closed

## Error Handling

- Database connection errors are caught and displayed
- User input validation prevents invalid choices
- Graceful handling of keyboard interrupts (Ctrl+C)
- General exception handling for unexpected errors
- Proper cleanup of database connection on program exit

## Menu System Features

- Clear visual separation with "=" lines
- Numbered options for easy selection
- Clear prompts for user input
- Invalid input handling with helpful error messages
- Consistent navigation between modes