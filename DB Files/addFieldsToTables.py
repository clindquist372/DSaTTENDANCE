# Assuming your table is named 'dragons'
table_name = 'CUSTOMER'

try:
    print(f"\n--- Fields (Columns) in the '{table_name}' Table ---")
    cursor.execute(f"PRAGMA table_info({table_name})")
    fields = cursor.fetchall()
    
    # The output format is (cid, name, type, notnull, dflt_value, pk)
    for field in fields:
        # We are mainly interested in the name and type
        print(f"Name: {field[1]}, Type: {field[2]}, Primary Key: {'Yes' if field[5] == 1 else 'No'}")

except sqlite3.OperationalError:
    print(f"Error: Table '{table_name}' does not exist.")
except sqlite3.Error as e:
    print(f"An error occurred while reading fields: {e}")
