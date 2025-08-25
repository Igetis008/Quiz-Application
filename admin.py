from database import add_question, get_all_questions, update_question

def admin_menu(connection):
    """Display and handle the admin menu"""
    while True:
        print("\n" + "="*50)
        print("ADMIN MODE")
        print("="*50)
        print("1. Add a new question")
        print("2. View all questions")
        print("3. Edit a question")
        print("4. Exit admin mode")
        print("-"*50)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_new_question(connection)
        elif choice == "2":
            view_all_questions(connection)
        elif choice == "3":
            edit_question(connection)
        elif choice == "4":
            print("Exiting admin mode...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

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

def edit_question(connection):
    """Edit an existing question in the database"""
    print("\n" + "="*50)
    print("EDIT QUESTION")
    print("="*50)
    
    # First, show all questions so the user can select which one to edit
    questions = get_all_questions(connection)
    
    if not questions:
        print("No questions found in the database.")
        return
    
    # Display all questions with their IDs
    print("Available questions:")
    for question in questions:
        print(f"ID: {question[0]} - {question[2][:50]}...")  # Show first 50 characters of question
    
    # Get the question ID to edit
    while True:
        try:
            question_id = int(input("\nEnter the ID of the question to edit: "))
            # Check if the ID exists
            question_exists = any(q[0] == question_id for q in questions)
            if question_exists:
                break
            else:
                print("Invalid ID. Please enter a valid question ID from the list above.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Find the selected question
    selected_question = None
    for question in questions:
        if question[0] == question_id:
            selected_question = question
            break
    
    # Display the current question details
    print(f"\nCurrent question details:")
    print(f"Category: {selected_question[1]}")
    print(f"Question: {selected_question[2]}")
    print(f"A: {selected_question[3]}")
    print(f"B: {selected_question[4]}")
    print(f"C: {selected_question[5]}")
    print(f"D: {selected_question[6]}")
    print(f"Answer: {selected_question[7]}")
    
    # Get new values (press Enter to keep current value)
    print("\nEnter new values (press Enter to keep current value):")
    category = input(f"Category ({selected_question[1]}): ").strip()
    category = category if category else selected_question[1]
    
    question_text = input(f"Question ({selected_question[2]}): ").strip()
    question_text = question_text if question_text else selected_question[2]
    
    option_a = input(f"Option A ({selected_question[3]}): ").strip()
    option_a = option_a if option_a else selected_question[3]
    
    option_b = input(f"Option B ({selected_question[4]}): ").strip()
    option_b = option_b if option_b else selected_question[4]
    
    option_c = input(f"Option C ({selected_question[5]}): ").strip()
    option_c = option_c if option_c else selected_question[5]
    
    option_d = input(f"Option D ({selected_question[6]}): ").strip()
    option_d = option_d if option_d else selected_question[6]
    
    # Get the correct answer
    while True:
        answer_input = input(f"Correct answer ({selected_question[7]}): ").strip()
        if not answer_input:  # Keep current answer
            answer = selected_question[7]
            break
        else:
            answer = answer_input.upper()
            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
    
    # Import the update function
    from database import update_question
    
    # Update the question in the database
    if update_question(connection, question_id, category, question_text, option_a, option_b, option_c, option_d, answer):
        print("Question updated successfully!")
    else:
        print("Failed to update question.")