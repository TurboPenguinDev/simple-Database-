import json
import os
 
DB_FILE = "database.json"
 
def load_db() -> list:
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [["Admin", "Root", "ROOT", 0, "-", "-"]]
 
def save_db(db: list) -> None:
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
 
def is_user(db: list,name: str):
    for user in db:
        if user[1] == name:
            return True
    return False
 
def get_user(db: list,name: str):
    for user in db:
        if user[1] == name:
            return user
    return None

def cmp_pw(db: list,name: str,password: str):
    for user in db:
        if user[1] == name and user[2] == password:
            return True
    return False

def cmd_quit(state):
    state["running"] = False

def cmd_add(state):
    current = get_user(state["db"], state["currentuser"])

    if current[0] not in ("Admin", "Moderator", "Editor"):
        print("You do not have the neccessary rights!")
    else:
        user = []
        print("Rights: ",end="")
        right = input().capitalize()
        user.append(right)

        if right not in ("Admin", "Editor", "Read-only", "Moderator"):
            print("This Role does not exist!")
            
        else:
            print("Name: ",end="")
            name = input().capitalize()
            user.append(name)
        
            print("Password: ",end="")
            password = input()
            user.append(password)
        
            print("Age: ",end="")
            age = input()
            user.append(int(age))
        
            print("Email: ",end="")
            email = input()
            user.append(email)
        
            print("Address: ",end="")
            address = input().capitalize()
            user.append(address)
        
            # 0 1 2 3 4 5
            # [RIGHTS] [NAME] [PASSWORD] [AGE] [EMAIL] [ADDRESS]
            state["db"].append(user)
            save_db(state["db"])

def cmd_print(state):
    print("What user do u want to print?\n> ", end="")
    name = input()

    for user in state["db"]:
        if name == user[1]:
            print()
            print("Rights: \t" + user[0])
            print("Name: \t\t" + user[1])
            print("Password: \t" + user[2])
            print("Age: \t\t" + str(user[3]))
            print("Email: \t\t" + user[4])
            print("Address: \t" + user[5])

def cmd_edit(state):
    if state["currentuser"] == ("Admin") or ("Moderator"):
        pass
    else:
        print("You do not have the neccessary rights!")

    edited_user = input("Which user do you want to edit: ")
    user = get_user(state["db"], edited_user)
    
    if user is None:
        print("User not found!")
    else:
        print("What do you want to enter")
        print("1: Rights 2: Name 3: Password 4: Age 5: Email 6: Address")
        
        field = input("Selection: ")
        if field == "1":
            user[0] = input("Neue Rechte: ")
        elif field == "2":
            user[1] = input("Neuer Name: ")
        elif field == "3":
            user[2] = input("Neues Passwort: ")
        elif field == "4":
            user[3] = input("Neues Alter: ")
        elif field == "5":
            user[4] = input("Neue Email: ")
        elif field == "6":
            user[5] = input("Neue Adresse: ")
        else:
            print("Invalid Selection!")

        print("User updated successfully!")
        save_db(state["db"])

def cmd_logout(state):
    state["currentuser"] = ""

def cmd_pwu(state):
    pwuser = input("Which user do u want to find (please enter only the name)? \nUser: ")
    user = get_user(state["db"], pwuser)

    if user == None:
        print("Error: User not found!")
    else:
        print("")
        print("Rights: " + user[0])
        print("Name:" + user[1])
        print("Password: " + user[2])
        print("Age: " + str(user[3]))
        print("Email: " + user[4])
        print("Address: " + user[5])

def cmd_find(state) : 
    print("What do you want to search?")
    print("1: Rights 2: Name 3: Age 4: Email 5: Address")
    
    field = int(input("Catagory: ")) - 1
    value = input("Value: ")
    
    print("What do you want to be displayed? (multiple with colon: 1,2,4)")
    print("1: Rights 2: Name 3: Password 4: Age 5: Email 6: Address")
    
    output_fields = input("Output: ").split(",") # → ["1", "2", "4"]
    field_names = ["Rights", "Name", "Password", "Age", "Email", "Address"]

    for user in state["db"]:
        if str(user[field]).lower() == value.lower():
            print("")
            for f in output_fields:
                index = int(f) - 1
                print(field_names[index] + ": " + str(user[index]))

def cmd_change (state):
    print("Password of the current user: ")
    password = input()

    
    
    if not cmp_pw(state["db"],username,password):
        print("Error: password does not match user!")
        print("-------------------------\n")
        return
    
    state["currentuser"] = input("Please enter the user u want to change to: ")
    print("Password: ",end="")
    password = input()
    
    if not cmp_pw(state["db"],username,password):
        print("Error: password does not match user!")
        print("-------------------------\n")
        return
 
def cmd_status(state):
    user = get_user(state["db"], state["currentuser"])
    print("")
    print("Rights: " + user[0])
    print("Name:" + user[1])
    print("Password: " + user[2])
    print("Age: " + str(user[3]))
    print("Email: " + user[4])
    print("Address: " + user[5])


def main():
    # 0 1 2 3 4 5
    # [RIGHTS] [NAME] [PASSWORD] [AGE] [EMAIL] [ADDRESS]
    
    state = {
        "running": True,
        "db": load_db(),
        "currentuser": ""
        "username"
    }
    
    while state["running"]:
        print("---- Database System ----")
        if state["currentuser"] == "":
            print("username: ",end="")
            username = input().capitalize()
 
            if not is_user(state["db"],username):
                print("Error: not a registered user!")
                print("-------------------------\n")
                continue
 
            print("password: ",end="")
            password = input()
 
            if not cmp_pw(state["db"],username,password):
                print("Error: password does not match user!")
                print("-------------------------\n")
                continue
 
            

            state["currentuser"] = username
            continue
 
        print("1: Quit")
        print("2: Login 3: Logout 4: Change 5: Status")
        print("6: Add 7: Edit 8: Print 9: Pwu")
        print("10: Find")
        print("-------------------------")
        print("Selection: ",end="")

        cmd = input().lower()
 
        if cmd == "quit":
            cmd_quit(state)
        elif cmd == "add":
            cmd_add(state)
        elif cmd =="print":
            cmd_print(state)
        elif cmd == "edit":
            cmd_edit(state)
        elif cmd == "logout":
            cmd_logout(state)
        elif cmd == "pwu":
            cmd_pwu(state)
        elif cmd == "find":
           cmd_find(state)
        elif cmd == "change":
            cmd_change(state)
        elif cmd == "status":
            cmd_status(state)
 
        print("-------------------------\n")
 
if __name__ == '__main__':
    main()