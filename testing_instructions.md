# Testing Instructions for Quiz System

## Prerequisites

1. **MySQL Server**: Ensure MySQL server is installed and running on your system
2. **Python**: Ensure Python 3.x is installed
3. **MySQL Connector**: Install the MySQL connector for Python:
   ```
   pip install mysql-connector-python
   ```

## Database Setup

1. **Create Database and Table**:
   - Open MySQL Workbench or any MySQL client
   - Execute the SQL commands from `database_setup.md` to create the database and table

2. **Verify Database Structure**:
   - The database should be named `quizdb`
   - The table should be named `questions` with the following columns:
     - id (INT, AUTO_INCREMENT, PRIMARY KEY)
     - category (TEXT)
     - question (TEXT)
     - option_a (TEXT)
     - option_b (TEXT)
     - option_c (TEXT)
     - option_d (TEXT)
     - answer (CHAR(1))

## Configuration

1. **Update Database Credentials**:
   - Open `database.py`
   - Update the `user` and `password` fields in the `create_connection()` function with your actual MySQL credentials

## Running the Program

1. **Start the Program**:
   - Open a terminal/command prompt
   - Navigate to the directory containing the Python files
   - Run the main program:
     ```
     python main.py
     ```

2. **Expected Output**:
   - Welcome message should be displayed
   - Database connection success message should appear
   - Main menu should be displayed with options for Admin Mode, Player Mode, and Exit

## Testing Admin Mode

1. **Select Admin Mode**:
   - Enter "1" at the main menu prompt

2. **Add a New Question**:
   - Select option "1" to add a new question
   - Enter category, question text, 4 options, and correct answer
   - Verify that "Question added successfully!" message is displayed

3. **View All Questions**:
   - Select option "2" to view all questions
   - Verify that all questions (including the newly added one) are displayed correctly

4. **Edit a Question**:
   - Select option "3" to edit a question
   - Select a question ID from the list
   - Modify some fields (or press Enter to keep current values)
   - Verify that "Question updated successfully!" message is displayed

5. **Exit Admin Mode**:
   - Select option "4" to exit admin mode
   - Verify that you return to the main menu

## Testing Player Mode

1. **Select Player Mode**:
   - Enter "2" at the main menu prompt

2. **Category Selection**:
   - Verify that all available categories are displayed
   - Select a category by entering the corresponding number

3. **Quiz Taking**:
   - Verify that 5 random questions from the selected category are displayed
   - Answer each question with A, B, C, or D
   - Verify that immediate feedback is provided for each answer

4. **Score Display**:
   - Verify that the final score is displayed with percentage
   - Verify that personalized feedback is provided based on the score

5. **Continuous Play with Category Selection**:
   - After the first quiz, verify that you're asked if you want to play another quiz
   - Select "Y" to continue playing
   - Verify that you see a confirmation message and then the category selection menu again
   - Select the same or a different category for the next quiz
   - Continue playing and selecting categories as desired
   - Select "N" when you want to return to the main menu

## Error Handling Testing

1. **Invalid Menu Choices**:
   - Enter invalid choices at menus and verify appropriate error messages

2. **Invalid Answer Inputs**:
   - Enter invalid answers (not A/B/C/D) and verify appropriate error messages

3. **Database Connection Failure**:
   - Temporarily provide incorrect database credentials and verify error handling

## Expected Features Verification

- [ ] Menu-driven interface works correctly
- [ ] Input validation prevents invalid entries
- [ ] Random question selection works
- [ ] Score tracking and calculation is accurate
- [ ] Clean terminal output with proper formatting
- [ ] Error handling works for various scenarios
- [ ] Database operations (INSERT, SELECT) work correctly

## Troubleshooting

1. **Database Connection Issues**:
   - Verify MySQL server is running
   - Check database credentials in `database.py`
   - Ensure `quizdb` database and `questions` table exist

2. **Module Import Errors**:
   - Ensure all Python files are in the same directory
   - Verify Python path is set correctly

3. **SQL Errors**:
   - Verify database structure matches the expected schema
   - Check for any typos in SQL commands

## Completion

After successfully testing all features, the quiz system is ready for use. You can:
- Add more questions using Admin Mode
- Take quizzes on different categories using Player Mode
- Extend the system with additional features as needed