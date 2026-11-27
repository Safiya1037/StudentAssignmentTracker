
assignments = []

def add_assignment(title, due_date):
    assignment = {
        "title": title,
        "due_date": due_date,
        "status": "Pending"
    }
    assignments.append(assignment)
    return assignment

def view_assignments():
    return assignments

def mark_completed(index):
    if 0 <= index < len(assignments):
        assignments[index]["status"] = "Completed"
        return True
    return False

def main():
    while True:
        print("\n--- Student Assignment Tracker ---")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter assignment title: ")
            due_date = input("Enter due date: ")
            add_assignment(title, due_date)
            print("Assignment added successfully!")

        elif choice == "2":
            if not assignments:
                print("No assignments available.")
            else:
                for i, assignment in enumerate(assignments, 1):
                    print(i, assignment)

        elif choice == "3":
            for i, assignment in enumerate(assignments, 1):
                print(i, assignment)

            try:
                index = int(input("Enter assignment number: "))
                if mark_completed(index - 1):
                    print("Assignment marked as completed!")
                else:
                    print("Invalid assignment number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
