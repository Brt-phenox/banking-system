

def run(users):
    admin_password=input("Enter Password : ")
    
    #admin password
    if admin_password !="admin123":
        print("Wrong Password")
    else:
        print("--------------------")   
        print("WELCOME ADMIN")

    while True:
        print("--------------------")
        print()
        print("1:See all users")
        print("2:Ban an user")
        print("3:Unban an user")
        print("4:Exit")
        print("---------------------")
        print()
        choice=input("Choose the option")

        if choice =="1":
            print("--ALL users list--")
            for name,display in users.items():
                print("User:", name)
                print("Balance:", display["balance"])
                print("Banned:", display["banned"])
                print()
        
        elif choice =="2":
            user_ban=input("Enter  user name to ban")
            if user_ban in users:
                users[user_ban]["banned"] = True
                print("*/----",user_ban, "is now banned ----/*")
            else:
                print("User not found")

        elif choice=="4":
            break 

        else:
            print("invalid")


      


       



     





            