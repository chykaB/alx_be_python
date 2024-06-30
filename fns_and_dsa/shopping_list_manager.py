# shopping_list = []
# choice1 = "add "
# choice2 = "remove"
# choice3 = "view"
# choice4 = "exit"

# if choice1:
#     shopping_list.append()
# elif choice2:
#     shopping_list.pop()
# elif choice3:
#     print(shopping_list)
# elif choice4:
#     print("Goodbye")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")


        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added")
           
        elif choice == '2':
            # Prompt for and remove an item
            item = input("what do you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list")
            else:
                print(f"{item} is not in the shopping list")
            
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index} {item}")
            else:
                print("your shopping list is empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()