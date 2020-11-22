import reminder, credential, json

def remindite():
    with open("reminder.json", "r") as f:
        remindite = json.load(f)
    
    on = True
    while on:
        for key, value in remindite.items():
            print(key, f"\n{value}")
            
        opt = int(input("""
        1. add category
        2. add reminder
        3. remove category
        4. remove reminder
        5. Edit date of reminder
        6. Quit
        """))

        if opt == 1: 
            reminder.Remind().add_category(remindite, input("Category:"))
            
            with open("reminder.json", "w") as f:
                json.dump(remindite,f)

        elif opt == 2:
            reminder.Remind().add_reminder(remindite, input("Catergory:"), input("Reminder:"), input("Date:"))
            
            with open("reminder.json", "w") as f:
                json.dump(remindite,f)
        
        elif opt == 3: 
            reminder.Remind().rm_category(remindite, input("Category:"))
            
            with open("reminder.json", "w") as f:
                json.dump(remindite,f)

        elif opt == 4:
            reminder.Remind().rm_reminder(remindite, input("Catergory:"), input("Reminder:"))
            
            with open("reminder.json", "w") as f:
                json.dump(remindite,f)
        
        elif opt == 5:
            reminder.Remind().change_date(remindite, input("Catergory:"), input("Reminder:"), input("New Date:"))
            
            with open("reminder.json", "w") as f:
                json.dump(remindite,f)
        
        elif opt == 6:
            quit()

def login():
    on = True
    while on:
        on = False
        print("Login")
        username = input("Username:")
        if username in file:
            p = False
            while not p:
                p = True
                if credential.Login().check_password(input("Password:"), file[username]): remindite()
                else: 
                    opt = int(input("""
                    Wrong Password
                    1. Try again
                    2. Forget Password
                    """
                    ))
                    
                    if opt == 1: p = False
                    elif opt == 2: 
                        file[username] = int(input("New Password:"))
        else: on = True
                    

def sign_up():
    print("Sign Up")
    username = credential.Sign_up().username(input("Username:"))
    
    password = credential.Sign_up().password(input("Password:"))

    file[username] = password
   
    with open("credential.json", "w") as f:
        json.dump(file, f)

    login()


def menu(): 

    on = True

    while on:
        on = False
        option = int(input("""
                    Welcome to Remindite!
            Please choose from the following options
                1. Sign in
                2. Sign up
                3. Quit
        """))

        if option == 1: login()
        elif option == 2: sign_up()
        elif option == 3: quit()

    
def main():
    with open("credential.json","r") as f:
        global file
        file = json.load(f)
    
    menu()


if __name__ == "__main__":
    main()