import json
import os

DATABASE = "data_store.json"

def load_data():
    if not os.path.exists(DATABASE):
        return []
    with open(DATABASE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)

def validate_record(record):
    if not record.get("id"):
        return False
    if not record.get("name"):
        return False
    if not record.get("email") or "@" not in record["email"]:
        return False
    return True

def is_duplicate(record, database):
    for data in database:
        if data["id"] == record["id"]:
            return True
    return False

def add_record(record):
    database = load_data()

    if not validate_record(record):
        print("Invalid data. Entry rejected.")
        return

    if is_duplicate(record, database):
        print("Duplicate data found. Entry blocked.")
        return

    database.append(record)
    save_data(database)

    print("Data added successfully.")

if __name__ == "__main__":
    # User input now, not hard-coded sample
    record = {}
    record["id"] = input("Enter ID: ")
    record["name"] = input("Enter Name: ")
    record["email"] = input("Enter Email: ")

    add_record(record)

