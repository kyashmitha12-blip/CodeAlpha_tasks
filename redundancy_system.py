import json
import os

DATABASE = "data_store.json"

def load_data():
    if not os.path.exists(DATABASE):
        return []
    with open(DATABASE, "r") as file:
        return json.load(file)

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

def generate_hash(record):
    raw = f"{record['id']}-{record['email']}"
    return hashlib.sha256(raw.encode()).hexdigest()

def is_redundant(record, database):
    record_hash = generate_hash(record)
    for data in database:
        if data["hash"] == record_hash:
            return True
    return False

def add_record(record):
    database = load_data()

    if not validate_record(record):
        print("Invalid data. Entry rejected.")
        return

    if is_redundant(record, database):
        print("Duplicate data found. Entry blocked.")
        return

    record["hash"] = generate_hash(record)
    database.append(record)
    save_data(database)

    print("Data added successfully.")

if __name__ == "__main__":
    sample = {
        "id": "101",
        "name": "Sample User",
        "email": "sample@gmail.com"
    }
    add_record(sample)
