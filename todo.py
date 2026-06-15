import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet!\n")
        return
    print("\n📋 Your Tasks:")
    print("-" * 30)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"✅ Added: '{title}'")
    else:
        print("⚠️  Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        task = tasks[num - 1]
        task["done"] = True
        save_tasks(tasks)
        print(f"🎉 Marked done: '{task['title']}'")
    except (ValueError, IndexError):
        print("⚠️  Invalid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"🗑️  Deleted: '{removed['title']}'")
    except (ValueError, IndexError):
        print("⚠️  Invalid number.")

def main():
    print("=" * 30)
    print("   🗒️  CLI To-Do App")
    print("=" * 30)
    tasks = load_tasks()

    while True:
        print("\nWhat do you want to do?")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Bye!\n")
            break
        else:
            print("⚠️  Invalid choice.")

if __name__ == "__main__":
    main()
