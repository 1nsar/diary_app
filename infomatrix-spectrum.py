# Welcome to the Personal Diary
print("Welcome to the Personal Diary, to create a new diary memory input your message!")

import json
import os
from datetime import datetime

diary_file = "diary.json"


def load_entries():
    if os.path.exists(diary_file):
        with open(diary_file, "r") as file:
            return json.load(file)
    return []


def save_entries(entries):
    with open(diary_file, "w") as file:
        json.dump(entries, file, indent=4)


def add_entry():
    title = input("Enter title: ")
    content = input("Enter content: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries = load_entries()
    entry = {"id": len(entries) + 1, "title": title, "date": date, "content": content}
    entries.append(entry)
    save_entries(entries)
    print("Entry added successfully!")


def list_entries():
    entries = load_entries()
    if not entries:
        print("No diary entries found.")
        return
    for entry in entries:
        print(f"[{entry['id']}] {entry['date']} - {entry['title']}")


def view_entry():
    entry_id = int(input("Enter entry ID: "))
    entries = load_entries()
    entry = next((e for e in entries if e["id"] == entry_id), None)
    if entry:
        print(f"\nTitle: {entry['title']}\nDate: {entry['date']}\nContent: {entry['content']}\n")
    else:
        print("Entry not found.")


def update_entry():
    entry_id = int(input("Enter entry ID to update: "))
    entries = load_entries()
    for entry in entries:
        if entry["id"] == entry_id:
            entry["title"] = input("Enter new title: ") or entry["title"]
            entry["content"] = input("Enter new content: ") or entry["content"]
            save_entries(entries)
            print("Entry updated successfully!")
            return
    print("Entry not found.")


def delete_entry():
    entry_id = int(input("Enter entry ID to delete: "))
    entries = load_entries()
    entries = [e for e in entries if e["id"] != entry_id]
    save_entries(entries)
    print("Entry deleted successfully!")


def main():
    while True:
        print("\nPersonal Diary - Spectrum Team")
        print("1. Create Entry")
        print("2. List Entries")
        print("3. View (display) Entry")
        print("4. Update Entry")
        print("5. Delete Entry")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            view_entry()
        elif choice == "4":
            update_entry()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



