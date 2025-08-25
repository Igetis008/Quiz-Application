# Database Connection Setup

## Installing MySQL Connector

For this quiz system, we'll use the official MySQL connector for Python. Install it using pip:

```bash
pip install mysql-connector-python
```

## Database Connection Implementation

Create a file named `database.py` with the following code:

```python
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='quizdb',
            user='root',  # Change this to your MySQL username
            password='password'  # Change this to your MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def add_question(connection, category, question, option_a, option_b, option_c, option_d, answer):
    """Add a new question to the database"""
    try:
        cursor = connection.cursor()
        query = """INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, answer) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (category, question, option_a, option_b, option_c, option_d, answer)
        cursor.execute(query, values)
        connection.commit()
        print("Question added successfully!")
        return True
    except Error as e:
        print(f"Error while adding question: {e}")
        return False
    finally:
        if cursor:
            cursor.close()

def get_all_questions(connection):
    """Retrieve all questions from the database"""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM questions"
        cursor.execute(query)
        questions = cursor.fetchall()
        return questions
    except Error as e:
        print(f"Error while fetching questions: {e}")
        return []
    finally:
        if cursor:
            cursor.close()

def get_categories(connection):
    """Get all distinct categories from the database"""
    try:
        cursor = connection.cursor()
        query = "SELECT DISTINCT category FROM questions"
        cursor.execute(query)
        categories = [row[0] for row in cursor.fetchall()]
        return categories
    except Error as e:
        print(f"Error while fetching categories: {e}")
        return []
    finally:
        if cursor:
            cursor.close()

def get_random_questions(connection, category, limit=5):
    """Get random questions from a specific category"""
    try:
        cursor = connection.cursor()
        query = """SELECT id, question, option_a, option_b, option_c, option_d, answer 
                   FROM questions 
                   WHERE category = %s 
                   ORDER BY RAND() 
                   LIMIT %s"""
        cursor.execute(query, (category, limit))
        questions = cursor.fetchall()
        return questions
    except Error as e:
        print(f"Error while fetching random questions: {e}")
        return []
    finally:
        if cursor:
            cursor.close()

def close_connection(connection):
    """Close the database connection"""
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
```

## Configuration Notes

1. Make sure to update the `user` and `password` fields in the `create_connection()` function with your actual MySQL credentials.
2. The default host is `localhost`, which should work if MySQL is running on your local machine.

3. The database name is set to `quizdb` as per our earlier setup.
