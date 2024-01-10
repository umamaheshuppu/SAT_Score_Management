import json

# In-memory storage for SAT results
sat_data = {}

def insert_data():
    print("Insert Data:")
    name = input("Name: ")
    address = input("Address: ")
    city = input("City: ")
    country = input("Country: ")
    pincode = input("Pincode: ")
    sat_score = float(input("SAT Score: "))

    passed = "Pass" if sat_score > 30 else "Fail"

    sat_data[name] = {
        'Name': name,
        'Address': address,
        'City': city,
        'Country': country,
        'Pincode': pincode,
        'SAT Score': sat_score,
        'Passed': passed
    }
    print("Data inserted successfully.")

def view_all_data():
    print("All Data:")
    for data in sat_data.values():
        print(json.dumps(data, indent=2))

def get_rank(name):
    sorted_data = sorted(sat_data.values(), key=lambda x: x['SAT Score'], reverse=True)
    rank = next((i + 1 for i, data in enumerate(sorted_data) if data['Name'] == name), None)
    
    if rank:
        print(f"{name}'s Rank: {rank}")
    else:
        print(f"No record found for {name}.")

def update_score(name):
    if name in sat_data:
        new_score = float(input(f"Enter new SAT Score for {name}: "))
        sat_data[name]['SAT Score'] = new_score
        sat_data[name]['Passed'] = "Pass" if new_score > 30 else "Fail"
        print(f"SAT Score updated for {name}.")
    else:
        print(f"No record found for {name}.")

def delete_record(name):
    if name in sat_data:
        del sat_data[name]
        print(f"Record for {name} deleted.")
    else:
        print(f"No record found for {name}.")

def export_to_json():
    with open('sat_results.json', 'w') as json_file:
        json.dump(list(sat_data.values()), json_file, indent=2)
    print("Data exported to JSON successfully.")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Insert Data")
    print("2. View All Data")
    print("3. Get Rank")
    print("4. Update Score")
    print("5. Delete One Record")
    print("6. Export Data to JSON")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        insert_data()
    elif choice == '2':
        view_all_data()
    elif choice == '3':
        name = input("Enter name to get rank: ")
        get_rank(name)
    elif choice == '4':
        name = input("Enter name to update score: ")
        update_score(name)
    elif choice == '5':
        name = input("Enter name to delete record: ")
        delete_record(name)
    elif choice == '6':
        export_to_json()
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
