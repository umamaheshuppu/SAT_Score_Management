import sqlite3
import json

# Connect to SQLite database (or any other database of your choice)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS player_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')
conn.commit()

def insert_data(name, score):
    cursor.execute('INSERT INTO player_data (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    print("Data inserted successfully.")

def view_all_data():
    cursor.execute('SELECT * FROM player_data')
    data = cursor.fetchall()
    print("All Data:")
    for row in data:
        print(row)

def get_rank(name):
    cursor.execute('SELECT id FROM player_data WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        cursor.execute('SELECT COUNT(*) FROM player_data WHERE score > (SELECT score FROM player_data WHERE name = ?)', (name,))
        rank = cursor.fetchone()[0] + 1
        print(f"{name}'s Rank: {rank}")
    else:
        print(f"No record found for {name}.")

def update_score(name, new_score):
    cursor.execute('UPDATE player_data SET score = ? WHERE name = ?', (new_score, name))
    conn.commit()
    print(f"Score updated for {name}.")

def delete_record(name):
    cursor.execute('DELETE FROM player_data WHERE name = ?', (name,))
    conn.commit()
    print(f"Record for {name} deleted.")

def export_to_json():
    cursor.execute('SELECT * FROM player_data')
    data = cursor.fetchall()
    json_data = [{'id': row[0], 'name': row[1], 'score': row[2]} for row in data]
    
    with open('player_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
    print("Data exported to JSON successfully.")

# Example usage
insert_data("John", 150)
insert_data("Alice", 200)
view_all_data()
get_rank("John")
update_score("Alice", 250)
view_all_data()
delete_record("John")
view_all_data()
export_to_json()

# Close the database connection
conn.close()
