users = []

def sign_up():
    print("\nSIGN UP")
    name = input("Enter your name: ")
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    
    for user in users:
        if user['email'] == email:
            print("This email is already registered.\n")
            return
    
    
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    users.append(user)
    print("Sign-up Successful!\n")


def log_in():
    print("\nLOG IN")
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    
    for user in users:
        if user['email'] == email and user['password'] == password:
            print("Login Successful!\n")
            return
    
    print("Login failed. Incorrect email or password.\n")


def display_users():
    print("\nUSER LIST")
    if not users:
        print("No users signed up yet.\n")
    else:
        print(f"{'Name':<15}{'Email':<25}{'Password':<15}")
        print("-" * 55)
        for user in users:
            print(f"{user['name']:<15}{user['email']:<25}{'*' * len(user['password']):<15}")  # Hide password
        print()


def delete_user():
    print("\nDELETE USER")
    email = input("Enter the email of the user to delete: ")
    
    for user in users:
        if user['email'] == email:
            users.remove(user)
            print(f"User with email {email} deleted successfully.\n")
            return
    print("User not found.\n")


def main():
    while True:
        print("Choose an option:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Display All Users")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            sign_up()
        elif choice == '2':
            log_in()
        elif choice == '3':
            display_users()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main()
