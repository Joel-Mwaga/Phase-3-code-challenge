# Articles Management System

This project models the relationships between Authors, Articles, and Magazines, with data persisted in a SQL database. It allows users to manage authors, articles, and magazines, and provides functionality to query and manipulate this data.

## Project Structure

```
code-challenge/
├── lib/                # Main code directory
│   ├── models/         # Model classes for Authors, Articles, and Magazines
│   ├── db/             # Database components including connection and schema
│   ├── controllers/     # Optional: Business logic
│   ├── debug.py        # Interactive debugging
│   └── __init__.py     # Makes lib a package
├── tests/              # Test directory for unit tests
├── scripts/            # Helper scripts for database setup and queries
├── .gitignore          # Files and directories to ignore in Git
└── README.md           # Project documentation
```

## Setup Instructions

### Option 1: Using Pipenv
1. Install dependencies:
   ```
   pipenv install pytest sqlite3
   ```
2. Activate the virtual environment:
   ```
   pipenv shell
   ```

### Option 2: Using venv
1. Create a virtual environment:
   ```
   python -m venv env
   ```
2. Activate the virtual environment:
   - Mac/Linux:
     ```
     source env/bin/activate
     ```
   - Windows:
     ```
     env\Scripts\activate
     ```
3. Install dependencies:
   ```
   pip install pytest
   ```

### Database Setup
You can choose between SQLite (recommended for beginners) or PostgreSQL (more powerful).

#### SQLite Setup
In `lib/db/connection.py`, use the following code to set up the connection:
```python
import sqlite3

def get_connection():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    return conn
```

#### PostgreSQL Setup
1. Create a database in PostgreSQL:
   ```
   createdb articles_challenge
   ```
2. In `lib/db/connection.py`, use the following code:
```python
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        "dbname=articles_challenge user=your_username password=your_password"
    )
    conn.cursor_factory = RealDictCursor
    return conn
```

## Testing Your Code
Run `pytest` to verify your implementation. For debugging, use `python lib/debug.py` to start an interactive session. Set up the test database with:
```
python scripts/setup_db.py
```

## Deliverables
1. **Database Schema**: Create SQL tables for Authors, Articles, and Magazines with appropriate relationships.
2. **Python Classes**: Implement classes for Author, Article, and Magazine with necessary SQL methods.
3. **SQL Query Methods**: Implement various SQL queries within your model classes.
4. **Relationship Methods**: Implement methods to manage relationships between authors, articles, and magazines.
5. **Database Transactions**: Implement transaction handling with context managers.

## Bonus Challenges
1. Implement a method to find the magazine with the most articles.
2. Add database indexes to improve query performance.
3. Create a CLI tool for interactive querying.

## Version Control
Ensure to create a Git repository and commit your work incrementally with clear commit messages.

## Submission
Before submission, ensure all tests pass, the database schema is implemented, SQL queries are optimized, and the repository shows a clear progression of work through commits.