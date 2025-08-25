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
            password='Igetis11893'  # Change this to your MySQL password
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

def update_question(connection, question_id, category, question, option_a, option_b, option_c, option_d, answer):
    """Update an existing question in the database"""
    try:
        cursor = connection.cursor()
        query = """UPDATE questions
                   SET category=%s, question=%s, option_a=%s, option_b=%s, option_c=%s, option_d=%s, answer=%s
                   WHERE id=%s"""
        values = (category, question, option_a, option_b, option_c, option_d, answer, question_id)
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount > 0:
            print("Question updated successfully!")
            return True
        else:
            print("No question found with that ID.")
            return False
    except Error as e:
        print(f"Error while updating question: {e}")
        return False
    finally:
        if cursor:
            cursor.close()

def close_connection(connection):
    """Close the database connection"""
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")