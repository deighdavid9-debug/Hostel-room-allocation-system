allocations = []

def allocate_room():
    name = input("Enter student name: ")
    room = input("Enter room number: ")
    allocations.append({"name": name, "room": room})
    print("Room allocated")

def view_allocations():
    for allocation in allocations:
        print(allocation["name"], "- Room:", allocation["room"])

def main():
    while True:
        print("1. Allocate Room")
        print("2. View Allocations")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            allocate_room()
        elif choice == "2":
            view_allocations()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
