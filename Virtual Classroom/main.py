from virtual_classroom_manager import VirtualClassroomManager


def main():
    manager = VirtualClassroomManager()

    print("Welcome to the Virtual Classroom Manager!")

    while True:
        print("\nAvailable commands:")
        print("  1. Add Classroom")
        print("  2. Add Student")
        print("  3. List Students in a Classroom")
        print("  4. Schedule Assignment")
        print("  5. Submit Assignment")
        print("  6. Help")
        print("  7. Exit")

        user_input = input("Enter the number of your choice: ").strip()

        if not user_input:
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            class_name = input("Enter the name of the classroom: ").strip()
            manager.add_classroom(class_name)

        elif choice == 2:
            student_id = input("Enter the student ID: ").strip()
            class_name = input("Enter the name of the classroom: ").strip()
            manager.add_student(student_id, class_name)

        elif choice == 3:
            class_name = input("Enter the name of the classroom: ").strip()
            manager.list_students(class_name)

        elif choice == 4:
            class_name = input("Enter the name of the classroom: ").strip()
            assignment_details = input("Enter assignment details: ").strip()
            manager.schedule_assignment(class_name, assignment_details)

        elif choice == 5:
            student_id = input("Enter the student ID: ").strip()
            class_name = input("Enter the name of the classroom: ").strip()
            assignment_details = input("Enter assignment details: ").strip()
            manager.submit_assignment(student_id, class_name, assignment_details)

        elif choice == 6:
            continue

        elif choice == 7:
            print("Thank you for using the Virtual Classroom Manager.")
            break

        else:
            print("Invalid choice. Please choose a number from the available commands.")


if __name__ == "__main__":
    main()
