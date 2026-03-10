

def run(users):
    name = input("username:")
    pw = input("password:")

    if name not in users:
        print("User vetena")

    elif users[name]["password"] != pw:
        print("password milena")

    elif users[name]["banned"]:
        print("Ban vako chas")
    else:
        print("Welcome" + name)    

        while True:
            print("1. balance")
            print("2. Deposite")
            print("3. Exit")
            
            choice = input("Choose:")

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
 