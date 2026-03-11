import admin
import user

users = {
    "Test1":   {"password": "pass1", "balance": 500000, "banned": False},
    "Test2": {"password": "pass2", "balance": 500000, "banned": False},
    "Test3":   {"password": "pass3", "balance": 500000, "banned": False}
}
while True:

        print("1: Admin")
        print("2: User")
        print("---------------------")
        choice=input("Choose admin or user : ")

        if choice =="1":
            admin.run(users)

        elif choice =="2":
            user.run(users) 

        elif choice == "3":
            print("Good bye")
            break

        else:
            print("invalid option")
