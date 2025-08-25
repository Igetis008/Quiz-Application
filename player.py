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
    
    # Main player loop
    while True:
        # Display categories
        print("\nAvailable categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        # Let player select a category
        selected_category = None
        while selected_category is None:
            try:
                choice = int(input(f"\nSelect a category (1-{len(categories)}): "))
                if 1 <= choice <= len(categories):
                    selected_category = categories[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(categories)}.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Start the quiz
        start_quiz(connection, selected_category)
        
        # Ask if player wants to continue
        continue_playing = None
        while continue_playing not in ["Y", "YES", "N", "NO"]:
            continue_playing = input("\nDo you want to play another quiz? (Y/N): ").strip().upper()
            if continue_playing in ["Y", "YES"]:
                # Continue playing, go back to category selection
                print("\nGreat! Let's play another quiz.")
                # The loop will continue to the next iteration
            elif continue_playing in ["N", "NO"]:
                # Exit player mode and return to main menu
                print("Returning to main menu...")
                return
            else:
                print("Please enter Y (Yes) or N (No).")

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