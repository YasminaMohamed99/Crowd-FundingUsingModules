from AuthenticationSystem.Registration import register
from AuthenticationSystem.Login import login

while True:
    print("1)Login\n2)Register\n0)Exit")
    choice=int(input("Enter choice: "))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 0:
        break            
    else:
        print("Please enter correct choice")
        continue
    