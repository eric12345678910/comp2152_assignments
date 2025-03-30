# Import the random library to use for the dice later
import random
import os


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt





# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

        file.write(f"A total of {count_monsters_killed()} monsters have been killed\n")


# Account
def create_user(username, password):
    
    # Create accounts.txt if it doesn't already exist 
    if not os.path.exists("accounts.txt"):
        with open("accounts.txt", "w") as file:
            print("Creating accounts.txt file...")

    
    # Append account information to file
    with open("accounts.txt", "a+") as file:
            print("Appending to accounts.txt...")
            file.write(f"\n{username}::{password}")


def username_available(username):

    # Verify accounts.txt file exists 
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

            if(username_on_file != username):
                continue
            else:
                print(f"I'm sorry, we already have a {username}. Do you go by any other name?")
                return False

        print(f"I've never met a {username} in person before. Welcome aboard!") 
        return True
        
    
# Verify user's password matches the second entry
def verify_passwords_match(password, confirm_password):
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

            if(username == username_on_file and password == password_on_file):
                print("Account verified.")
                return True
            
        # No accounts match username and password
        print("Error: Invalid username or password.")
        return False



def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)

                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")




def count_monsters_killed():
    monstersKilled = 0
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                singleLine = line.split()
        
                if(singleLine[0] == "Hero"):
                    monstersKilled +=1
                else: continue

            return monstersKilled
            
    except FileNotFoundError:
        print("No previous game found.")
    return None
            


def read_monsters_killed():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
        
            monstersKilledMessage = ""

            for line in lines:
                if("A total of" in line):
                    monstersKilledMessage = line
                else: 
                    continue
            
            # Print last occurance of Total Monsters Killed message
            print(monstersKilledMessage)
            
    except FileNotFoundError:
        print("No previous game found.")
    return None

def playing_card(username):
    print("-------------------------------------------")
    print(f"The Hero {username}")
    print("Level: ") # relative to total monsters killed (or win/loss %) - maybe a combination of the two
                    # games played - experience - newbie, rookie, amateur, hobbiest, enthusiast
                    # win % = adjectives for success (top)
                    # total kills = adjectives for killer (slayer)


    print("Hero Ranking: ") # out of number out of total accounts
    print("Monsters killed: ")
    print("Win %: ")
    print("Damage delt: ")
    print("Damage taken: ")

    print("Weapon of choice: ")
    print("Sleep number") #most common level of sleep / total levels of sleep



    print("-------------------------------------------")