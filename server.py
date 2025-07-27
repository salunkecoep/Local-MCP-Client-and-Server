import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('EmployeesInformation')

def init_db():
    conn = sqlite3.connect('EmployeesData.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()

@mcp.tool()
def read_employee_data(query: str= "SELECT * FROM Employee" ) -> list:
    """Read data from the Employee table using a SQL SELECT query.

    Args:
        query (str, optional): SQL SELECT query. Defaults to "SELECT * FROM Employee".
            Examples:
                SELECT * FROM Employee;
                SELECT * FROM Employee WHERE age > 25;
                SELECT * FROM Employee WHERE name LIKE '%Amol%';
                SELECT * FROM Employee WHERE role LIKE '%Developer%';
                SELECT * FROM Employee ORDER BY age DESC;

        Please put single quotes around string literals like 'Amol', 'Developer'.
        
    Returns:
        list: List of tuples containing the query results.
            For default query, tuple format is (id, name, age, role)
    """

    try:
        print(query)
        conn = sqlite3.connect('EmployeesData.db')
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")
        return []
    finally:
        conn.close()

def add_data(name: str, age: int, role: str):
    query = f'INSERT INTO Employee (name, age, role) VALUES ("{name}", {age}, "{role}")'
    
    conn = sqlite3.connect('EmployeesData.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(f"Data added: {name}, {age}, {role}")

def delete_records():
    conn = sqlite3.connect('EmployeesData.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employee")
    conn.commit()
    conn.close()

def add_employee_records():
    add_data("Amol Salunke", 30, "Developer")
    add_data("Gautam Patil", 28, "QA Engineer")
    add_data("Saurabh Deshmukh", 35, "Project Manager")
    add_data("Neha Joshi", 26, "Tester")
    add_data("Riya Kulkarni", 32, "UX Designer")
    add_data("Pratik Shah", 29, "DevOps Engineer")
    add_data("Ananya Rao", 27, "Developer")
    add_data("Vikas Mehta", 31, "Tester")
    add_data("Pooja Nair", 33, "Scrum Master")
    add_data("Kiran Verma", 24, "Developer")
    add_data("Mitesh Jain", 34, "Tester")

if __name__ == "__main__":
     init_db()
     delete_records()
     add_employee_records()

     mcp.run('sse')

