import admin
import user
import json

# file handling
def load_users():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_users(users):
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

users =load_users()

#if no users exists creae default user
if not users:
    users = {
    "Test1":   {"password": "pass1", "balance": 500000, "banned": False},
    "Test2": {"password": "pass2", "balance": 500000, "banned": False},
    "Test3":   {"password": "pass3", "balance": 500000, "banned": False},
    "Test4":   {"password": "pass4", "balance": 500000, "banned": False}
    }
    save_users(users)

while True:
        print("---BANK MGMT SYSTEM---")
        print("----------------------")
        print("1: Admin")
        print("2: User (login/Register)")
        print("3:Exit")
        print("----------------------")
        choice=input("Choose admin or user :  ")

        if choice =="1":
            admin.run(users)
            save_users(users)

        elif choice =="2":
            user.run(users) 
            save_users(users)

        elif choice == "3":
            print(" THANK U")
            save_users(users)
            break

        else:
            print("invalid option")
