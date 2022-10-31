import level
import magic_number
import Account
import searchuser as sc
def Menu(Uname,AccBalance):
        print("Welcome back\nUsername:",Uname,"\nAccount Balance:",AccBalance)
        print("#############################__MENU__##############################")
        print("1- NEW GAME")
        print("2- Instructions")
        print("3- Logout")
        choice=int(input("Enter your choice here: "))
        while(choice!=1 and choice!=2 and choice!=3):
            print("invalid choice")
            choice=int(input("enter a valid selection: "))
        if(choice == 1):
            magic_number.game_party(level.level(), AccBalance, Uname)
        elif(choice == 2):
            magic_number.game_description(Uname, AccBalance)
        else:
            if Account.start()==1:
                sc.login(Account.Login())
            elif Account.start()==2:
                sc.registration(Account.Register())
            else:
                exit(0)