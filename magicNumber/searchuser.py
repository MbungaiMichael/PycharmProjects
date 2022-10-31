import filegesture as fg
import time
import Menu

def login(data):
    userList = fg.fileread("userList.data") # for user_name
    balanceList = fg.fileread("balance.data") # for balance
    passList = fg.fileread("pass.data") # for password
    if userList.count(data[0])==0 :
        print("user name not correct")
    elif passList.count(data[1])==0:
        print("Password not correct")
    else:
        Menu.Menu(data[0], balanceList[userList.index(data[0])])
       
def registration(data):
    userList = fg.fileread("userList.data")
    balanceList = fg.fileread("balance.data")
    passList = fg.fileread("pass.data")
    userList.append(data[0])
    balanceList.append(0)
    passList.append(data[1])
    fg.filewrite("userList.data", userList)
    fg.filewrite("balance.data", balanceList)
    fg.filewrite("pass.data", passList)
    print("Registration successful")
    time.sleep(1) # o read reg successful
    Menu.Menu(data[0], 0)