import reminder, credential, json

def remindite():
    pass


def login():
    on = True
    while on:
        on = False
        username = input("Username:")
        if username in file:
            p = False
            while not p:
                p = True
                password = int(input("Password:"))
                if credential.Login().check_password(password, file[username]): remindite()
                else: 
                    opt = int(input("""
                    Wrong Password
                    1. Try again
                    2. Forget Password
                    """
                    ))
                    
                    if opt == 1: p = False
                    elif opt == 2: 
                        file[username]
        else: on = True
                    


def sign_up():
    username = credential.Sign_up().username(input("Username:"))
    
    password = credential.Sign_up().password(int(input("Password:")))

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