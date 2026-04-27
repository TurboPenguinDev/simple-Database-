
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

def main():
    #  0        1       2         3     4       5
    # [RIGHTS] [NAME] [PASSWORD] [AGE] [EMAIL] [ADDRESS]
    db = [
        ["Admin","Root","ROOT",0,"-","-"]
    ]
    running = True
    currentuser = ""

    while running:
        
        print("---- Database System ----")
        
        if currentuser == "":
            print("username: ",end="")
            username = input().capitalize()
            if not is_user(db,username):
                print("Error: not a registered user!")
                print("-------------------------\n")
                continue
            
            print("password: ",end="")
            password = input()
            if not cmp_pw(db,username,password):
                print("Error: password does not match user!")
                print("-------------------------\n")
                continue

            currentuser = username
            continue
        
        print("1:  Quit")
        print("2:  Login   3: Logout   4: Change   5: Status")
        print("6:  Add     7: Edit     8: Print    9: Pwu")
        print("10: Find")
        print("-------------------------")
        print("Selection: ",end="")

        cmd = input().lower()

        if cmd == "quit":
            running = False
        elif cmd == "add":
            user = []

            print("Rights: ",end="")
            right = input().capitalize()
            user.append(right)
            if right not in ("Admin", "Editor", "Read-only", "Moderator"):
                print("This Role does not exist!")
                continue

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

            
             #  0        1       2         3     4       5
            # [RIGHTS] [NAME] [PASSWORD] [AGE] [EMAIL] [ADDRESS]
            db.append(user)

        elif cmd =="print":
            print("What user do u want to print? ", end="")
            name = input()

            for user in db:
                if name == user[1]:
                    print("")
                    print("Rights: " + user[0])
                    print("Name:" + user[1])
                    print("Password: " + user[2])
                    print("Age: " + str(user[3]))
                    print("Email: " + user[4])
                    print("Address: " + user[5])

        elif cmd == "edit":
            if user[0] == ("Admin") or ("Moderator"):
                pass
            else:
                print("You do not have the neccessary rights!")
            edited_user = input("Which user do you want to edit: ")
            user = get_user(db, edited_user)
    
            if user is None:
                print("User not found!")

            else:
                print("What do you want to enter")
                print("1: Rights  2: Name  3: Password  4: Age  5: Email  6: Address")
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

        elif cmd == "logout":
            currentuser = ""

        elif cmd == "pwu": 
            pwuser = input("Which user do u want to find (please enter only the name)? \nUser: ")
            user = get_user(db, pwuser)

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

        elif cmd == "find":
            print("What do you want to search?")
            print("1: Rights  2: Name  3: Age  4: Email  5: Address")
            field = int(input("Catagory: ")) - 1
            value = input("Value: ")

            print("What do you want to be displayed? (multiple with colon: 1,2,4)")
            print("1: Rights  2: Name  3: Password  4: Age  5: Email  6: Address")
            output_fields = input("Output: ").split(",")  # → ["1", "2", "4"]

            field_names = ["Rights", "Name", "Password", "Age", "Email", "Address"]

            for user in db:
                if str(user[field]).lower() == value.lower():
                    print("")
                    for f in output_fields:
                        index = int(f) - 1
                        print(field_names[index] + ": " + str(user[index]))

        elif cmd == "change":
            print("Password of the current user: ")
            password = input()
            if not cmp_pw(db,username,password):
                print("Error: password does not match user!")
                print("-------------------------\n")
                continue

            currentuser = input("Please enter the user u want to change to: ")

            print("Password: ",end="")
            password = input()
            if not cmp_pw(db,username,password):
                print("Error: password does not match user!")
                print("-------------------------\n")
                continue

        elif cmd == "status":
            user = get_user(db, currentuser)
            print("")
            print("Rights: " + user[0])
            print("Name:" + user[1])
            print("Password: " + user[2])
            print("Age: " + str(user[3]))
            print("Email: " + user[4])
            print("Address: " + user[5])

        print("-------------------------\n")

if __name__ == '__main__':
    main()
