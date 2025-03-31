import os

class User:
    # Initialize user
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Delete user object
    def __del__(self):
         print("User object is being deleted...")
         

    def create_user_account(self):
        # Create accounts.txt if it doesn't already exist 
        if not os.path.exists("accounts.txt"):
            with open("accounts.txt", "w") as file:
                print("Creating accounts.txt file...")

        # Append account information to file
        with open("accounts.txt", "a+") as file:
            print("Appending to accounts.txt...")
            file.write(f"\n{self.username}::{self.password}")

    # Check availability of username
    def username_available(self):
        # Create accounts.txt if one does not exist
        if not os.path.exists("accounts.txt"):    
            with open("accounts.txt", "w") as file:
                print("Creating accounts.txt file...")

            # If no file exists, all usernames are available
            return True
        

        with open("accounts.txt", "r") as file:
            print("Checking availability of username...")
            
            # Iterate through account file
            for line in file.readlines():
                print(f"line.strip(): {line.strip()}\n")

                # Taking the first position of [username, password]
                username_on_file = line.strip().split("::")[0]
                print(f"username_on_file: {username_on_file}")

                if(username_on_file == self.username):
                    print(f"I'm sorry, we already have a {self.username}. Do you go by any other name?")
                    return False
                
            print(f"I've never met a {self.username} in person before. Welcome aboard!") 
            return True
        
    # Verify user's password matches the second entry
    def confirm_password(password, confirm_password):
        if password == confirm_password:
            return True
        else:
            print("Error: Password do not match")
            return False
            
    # Verify user's account access
    def verify_user(username, password):
        # Verify accounts file exists.
        if not os.path.exists("accounts.txt"):
            print("Error: Accounts could not be found.")
            return False
        
        # Open and iterate through the acocunts file
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                # Assign username and passwords to variables
                username_on_file = line.strip().split("::")[0]
                password_on_file = line.strip().split("::")[1]

                # Return true when a match is found
                if(username == username_on_file and password == password_on_file):
                    print("Account verified.")
                    return True
                
            # No accounts match username and password
            print("Error: Invalid username or password.")
            return False

        