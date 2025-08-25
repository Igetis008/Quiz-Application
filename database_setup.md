# MySQL Database Setup for Quiz System

## Creating the Database and Table

Use the following SQL commands to create the database and table structure:

```sql
-- Create the quizdb database
CREATE DATABASE quizdb;

-- Use the quizdb database
USE quizdb;

-- Create the questions table
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

## Sample Questions Insertion

After creating the table, you can insert sample questions using these SQL commands:

```sql
-- Insert sample questions in History category
INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, answer) VALUES
('History', 'Who was the first President of the United States?', 'Thomas Jefferson', 'George Washington', 'Abraham Lincoln', 'John Adams', 'B'),
('History', 'In which year did World War II end?', '1943', '1945', '1950', '1939', 'B'),
('History', 'Which ancient civilization built the pyramids?', 'Romans', 'Greeks', 'Egyptians', 'Mesopotamians', 'C');

-- Insert sample questions in Science category
INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, answer) VALUES
('Science', 'What is the chemical symbol for gold?', 'Go', 'Gd', 'Au', 'Ag', 'C'),
('Science', 'What planet is known as the Red Planet?', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'B'),
('Science', 'What is the hardest natural substance on Earth?', 'Gold', 'Iron', 'Diamond', 'Platinum', 'C');

-- Insert sample questions in Literature category
INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, answer) VALUES
('Literature', 'Who wrote "Romeo and Juliet"?', 'Charles Dickens', 'William Shakespeare', 'Jane Austen', 'Mark Twain', 'B'),
('Literature', 'What is the pen name of Charles Dodgson?', 'Lewis Carroll', 'George Eliot', 'Mark Twain', 'Emily Brontë', 'A'),
('Literature', 'Which novel features the character Holden Caulfield?', 'To Kill a Mockingbird', 'The Great Gatsby', 'The Catcher in the Rye', 'Lord of the Flies', 'C');
```

You can run these commands in MySQL Workbench or any other MySQL client to set up your database.