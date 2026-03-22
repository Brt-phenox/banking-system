

def run(users):
    print("___________________")
    print(" || User System || ")
    print("___________________")

    print("1. login ")
    print("2. Register")
    print("3. Exit")

    option = input("Choose option")

    if option =="2":
        register(users)
        return
    elif option =="3":
        return
    elif option !="1":
        print("invalid option")
        return
    
    # login 
    print("___________________")
    print(" || HELLLO USER ||  ")
    print("-------------------")
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
          
          # user menu
        while True:
            print("1. Check balance")
            print("2. Deposite")
            print("3. Withdraw")
            print("4. Transaction history")
            print("5. Exit")
            
            choice = input("Choose:")
            print("----------------------")

            if choice == "1":
                print(users[name]["balance"])
            elif choice == "2":
                amount=float(input("Kati??"))
                users[name]["balance"] += amount
                print(users[name]["balance"])
            elif choice =="3":
                try:
                    amount = float(input("Enter withdraw amount: "))

                    if amount > users[name]["balance"]:
                      print("Insufficient balance ")
                      continue
                    
                    users[name]["balance"] -= amount
                    print("Remaining balance:", users[name]["balance"])
                    print("--------------------------")

                except:
                     print("Invalid input ")
            elif choice == "4":   
                print("\n----Transaction History----")
                for h in users[name]["history"]:
                    print("-",h)
            elif choice == "5" :
                break
            else :
                print("invalid")
#Registration page
def register(users):
    print("\n---User Register---")
    username = input("Enter username:")

    if username in users:
        print("**-- USERNAME ALREADY EXISTS --**")  
        return
    
    password = input ("Enter password:")
    users[username]={
                "password":password,
                "balance":0,
                "banned":False,
                "history":[]
            }          
 