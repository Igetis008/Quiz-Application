# Player Mode Implementation

## Player Module (player.py)

Create a file named `player.py` with the following code:

```python
from database import get_categories, get_random_questions

def player_menu(connection):
    """Display and handle the player menu"""
    print("\n" + "="*50)
    print("PLAYER MODE")
    print("="*50)
    
    # Get available categories
    categories = get_categories(connection)
    
    if not categories:
        print("No categories found. Please add questions first.")
        return
    
    # Display categories
    print("Available categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    # Let player select a category
    while True:
        try:
            choice = int(input(f"\nSelect a category (1-{len(categories)}): "))
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Start the quiz
    start_quiz(connection, selected_category)

def start_quiz(connection, category):
    """Start the quiz with questions from the selected category"""
    print(f"\n" + "="*50)
    print(f"QUIZ - Category: {category}")
    print("="*50)
    
    # Get 5 random questions from the selected category
    questions = get_random_questions(connection, category, 5)
    
    if not questions:
        print(f"No questions found for category: {category}")
        return
    
    # Initialize score
    score = 0
    total_questions = len(questions)
    
    # Ask questions one by one
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total_questions}:")
        print(question[1])  # Question text
        print(f"A. {question[2]}")  # Option A
        print(f"B. {question[3]}")  # Option B
        print(f"C. {question[4]}")  # Option C
        print(f"D. {question[5]}")  # Option D
        
        # Get player's answer
        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        # Check if answer is correct
        if answer == question[6]:  # Correct answer
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer is {question[6]}.")
    
    # Display final score
    display_score(score, total_questions)

def display_score(score, total_questions):
    """Display the final score"""
    print(f"\n" + "="*50)
    print("QUIZ RESULTS")
    print("="*50)
    print(f"Your score: {score}/{total_questions}")
    
    # Calculate percentage
    if total_questions > 0:
        percentage = (score / total_questions) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        # Provide feedback based on score
        if percentage >= 80:
            print("Excellent! Great job!")
        elif percentage >= 60:
            print("Good work! Keep it up!")
        elif percentage >= 40:
            print("Not bad! Try again to improve!")
        else:
            print("Keep practicing! You'll do better next time!")
    
    print("="*50)
```

## Key Features of Player Mode

1. **Category Selection**: Displays all available categories and lets the player choose one
2. **Random Question Selection**: Fetches 5 random questions from the selected category
3. **Question Presentation**: Shows questions and options in a clear format
4. **Input Validation**: Ensures player input is one of A/B/C/D
5. **Score Tracking**: Keeps track of correct answers
6. **Result Display**: Shows final score with percentage and feedback

## Usage Flow

1. User selects Player mode from the main menu
2. All available categories are fetched from the database and displayed
3. Player selects a category by entering the corresponding number
4. 5 random questions are fetched from the selected category
5. Questions are presented one by one with options A-D
6. Player inputs their answer (A/B/C/D) for each question
7. Immediate feedback is given for each answer (correct/incorrect)
8. Final score is displayed with percentage and personalized feedback