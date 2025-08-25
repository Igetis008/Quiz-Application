# Quiz System with MySQL Backend

A comprehensive quiz system with Admin and Player modes, using MySQL for data storage.

## Features

- **Admin Mode**: Add new questions and view existing questions
- **Player Mode**: Take quizzes on various categories
- **MySQL Backend**: Persistent storage of questions and categories
- **Input Validation**: Robust validation for all user inputs
- **Randomized Questions**: Different quiz experience each time
- **Score Tracking**: Automatic scoring with percentage and feedback

## Project Structure

```
quiz-system/
├── main.py          # Main program entry point
├── database.py      # Database connection and operations
├── admin.py         # Admin mode functionality
├── player.py        # Player mode functionality
├── utils.py         # Utility functions
├── database_setup.md # SQL commands for database setup
├── testing_instructions.md # Testing guide
└── README.md        # This file
```

## Prerequisites

- Python 3.x
- MySQL server
- mysql-connector-python library

## Installation

1. **Install MySQL Connector**:
   ```bash
   pip install mysql-connector-python
   ```

2. **Set Up Database**:
   - Open MySQL Workbench or another MySQL client
   - Execute the SQL commands from `database_setup.md` to create the database and insert sample questions

3. **Configure Database Connection**:
   - Edit `database.py` to set your MySQL username and password

## Usage

Run the program:
```bash
python main.py
```

### Admin Mode

1. Select "1" for Admin Mode
2. Choose from:
   - Add a new question
   - View all questions
   - Edit a question
   - Exit admin mode

### Player Mode

1. Select "2" for Player Mode
2. Choose a category from the list
3. Answer 5 random questions
4. View your score and feedback

## Database Schema

```sql
CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category TEXT,
    question TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    answer CHAR(1)
);
```

## Code Overview

### Main Components

- `main.py`: Entry point with main menu
- `database.py`: Database operations (connection, queries)
- `admin.py`: Admin functionality (add/view questions)
- `player.py`: Player functionality (take quizzes)
- `utils.py`: Utility functions for input validation

### Key Functions

- `create_connection()`: Establish MySQL connection
- `add_question()`: Insert new question into database
- `get_random_questions()`: Retrieve random questions by category
- `admin_menu()`: Admin mode interface
- `player_menu()`: Player mode interface

## Theory Explanations

The system demonstrates:

1. **MySQL Connection**: Using mysql-connector-python to connect to MySQL
2. **SQL Operations**: INSERT for adding questions, SELECT for retrieving questions
3. **Parameterized Queries**: Preventing SQL injection
4. **Menu System**: User-friendly interface with clear options
5. **Score Calculation**: Tracking and displaying quiz results

## Testing

Follow the instructions in `testing_instructions.md` to test all features:

- Admin mode functionality
- Player mode functionality
- Input validation
- Error handling
- Database operations

## Extending the System

You can extend this system by:

- Adding more categories and questions
- Implementing difficulty levels
- Adding a user registration system
- Creating a web interface
- Adding time limits to quizzes
- Implementing a leaderboard system
