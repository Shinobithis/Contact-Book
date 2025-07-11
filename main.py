def main():
    Handle()

def Menu():
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show all Contact")
    print("5. Exit")

    while True:
        try:
            choose = int(input("Please select an option (1-5): "))
            if choose < 1 or choose > 5:
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        if choose in [1, 2, 3, 4, 5]:
            return choose

def Handle():
    flag = True
    while flag:
        choose = Menu()

        if choose == 1:
            add_contact()
        elif choose == 2:
            search_contact()
        elif choose == 3:
            delete_contact()
        elif choose == 4:
            show_contacts()
        elif choose == 5:
            print("Exiting...")
            flag = False

def add_contact():
    with open('contact.txt', 'a') as file:
        name = input("Entre your Name: \n").lower()
        phone = input("Entre your Phone Number: \n")
        file.write(f"Name: {name} Phone: {phone}\n")

def search_contact():
    search = input("\nEnter the name or phone number to search: ").lower()
    found = False

    with open('contact.txt') as file:
        contacts = file.readlines()
        for line in contacts:
            if search in line:
                print(line.strip())
                found = True

    if not found:
        print("Contact not found.")

def delete_contact():
    search = input("\nEnter the name or phone number to Delete: ").lower()
    found = False

    with open('contact.txt') as file:
        contacts = file.readlines()

    new_contacts = []
    for line in contacts:
        if search not in line:
            new_contacts.append(line)
        else:
            found = True
    
    with open('contact.txt', 'w') as refile:
        refile.writelines(new_contacts)
    
    if found:
        print("Contact deleted successfully.")
    if not found:
        print("Contact not found.")


                
def show_contacts():
    with open('contact.txt') as file:
        contacts = file.readlines()
        for line in contacts:
            print(line.strip())

main()