import sqlite3
import sys

def create_table_from_input():
    # 1. Prompt the user for the desired table name
    table_name = input("Enter the desired name for your new table: ")

    # Basic input validation: Check if the table name is empty
    if not table_name:
        print("Error: Table name cannot be empty. Please try again.")
        return

    # 2. Define the database file name (UPDATED HERE)
    # The script will use 'dragon.db'. If it doesn't exist, it will be created.
    database_file = 'dragon.db' 

    # 3. Connect to the SQLite database
    conn = None
    try:
        # Connect to the database file
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # 4. Construct the SQL CREATE TABLE command
        sql_command = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            value REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """

        # 5. Execute the command
        cursor.execute(sql_command)

        # 6. Commit the changes to the database file
        conn.commit()

        print(f"\nSuccess! Table '{table_name}' has been created in '{database_file}'")
        print("Columns created: id (PK), name (TEXT), value (REAL), timestamp (DATETIME)")

    except sqlite3.Error as e:
        # Handle any SQLite-specific errors (e.g., if the name is an illegal SQL keyword)
        print(f"\nAn SQLite error occurred: {e}", file=sys.stderr)
    except Exception as e:
        # Handle other unexpected errors
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
    finally:
        # 7. Close the connection whether an error occurred or not
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table_from_input()