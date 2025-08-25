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