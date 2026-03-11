

def run(users):
    print("__________________")
    print(" | HELLLO USER |  ")
    print("-----------------")
    name = input("username:")
    pw = input("password:")
    print("-----------------")

    if name not in users:
        print("User not found enter valid user name")

    elif users[name]["password"] != pw:
        print("|password incorrect|")

    elif users[name]["banned"]:
        print("User id has been ban")
    else:
        print("Welcome" + name)    

        while True:
            print("1. balance")
            print("2. Deposite")
            print("3. Exit")
            
            choice = input("Choose:")
            print("----------------------")

            if choice == "1":
                print(users[name]["balance"])
            elif choice == "2":
                amount=float(input("Kati??"))
                users[name]["balance"] += amount
                print(users[name]["balance"])
            elif choice == "3" :
                break
            else :
                print("invalid")
 