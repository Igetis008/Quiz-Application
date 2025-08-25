# Admin Mode Implementation

## Admin Module (admin.py)

Create a file named `admin.py` with the following code:

```python
from database import add_question, get_all_questions

def admin_menu(connection):
    """Display and handle the admin menu"""
    while True:
        print("\n" + "="*50)
        print("ADMIN MODE")
        print("="*50)
        print("1. Add a new question")
        print("2. View all questions")
        print("3. Exit admin mode")
        print("-"*50)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            add_new_question(connection)
        elif choice == "2":
            view_all_questions(connection)
        elif choice == "3":
            print("Exiting admin mode...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def add_new_question(connection):
    """Add a new question to the database"""
    print("\n" + "="*50)
    print("ADD NEW QUESTION")
    print("="*50)
    
    category = input("Enter category (e.g., History, Science, Literature): ").strip()
    question = input("Enter the question: ").strip()
    option_a = input("Enter option A: ").strip()
    option_b = input("Enter option B: ").strip()
    option_c = input("Enter option C: ").strip()
    option_d = input("Enter option D: ").strip()
    
    # Get the correct answer
    while True:
        answer = input("Enter the correct answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    
    # Add the question to the database
    if add_question(connection, category, question, option_a, option_b, option_c, option_d, answer):
        print("Question added successfully!")
    else:
        print("Failed to add question.")

def view_all_questions(connection):
    """View all questions in the database"""
    print("\n" + "="*50)
    print("ALL QUESTIONS")
    print("="*50)
    
    questions = get_all_questions(connection)
    
    if not questions:
        print("No questions found in the database.")
        return
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(f"  ID: {question[0]}")
        print(f"  Category: {question[1]}")
        print(f"  Question: {question[2]}")
        print(f"  A: {question[3]}")
        print(f"  B: {question[4]}")
        print(f"  C: {question[5]}")
        print(f"  D: {question[6]}")
        print(f"  Answer: {question[7]}")
        print("-" * 30)
    
    print(f"\nTotal questions: {len(questions)}")
```

## Key Features of Admin Mode

1. **Menu-driven interface**: Clear options for adding questions, viewing questions, or exiting
2. **Input validation**: Ensures correct answer is one of A/B/C/D
3. **Error handling**: Gracefully handles database errors
4. **User-friendly display**: Formats questions in a readable way when viewing all questions

## Usage Flow

1. User selects Admin mode from the main menu
2. Admin menu is displayed with three options:
   - Add a new question
   - View all questions
   - Exit admin mode
3. For adding questions:
   - Prompt for category, question text, and 4 options
   - Validate that answer is A/B/C/D
   - Insert into database using database.add_question()
4. For viewing questions:
   - Retrieve all questions using database.get_all_questions()
   - Display in a formatted way
5. Admin can continue using the menu until they choose to exit