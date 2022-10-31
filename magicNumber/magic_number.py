# -*- coding: utf-8 -*-
import random
import Menu
import filegesture as fg


def level_select():
    print("   1. Easy   ...... 15Points")
    print("   2. Medium ...... 10Points")
    print("   3. Hard   ...... 5Points")
    print("   4. Extreme...... 3Points")
    print("Select a level")
    choice = int(input())
    if(choice == 1):
        points = 15
    elif(choice==2):
        points = 10
    elif(choice==2):
        points = 5
    elif(choice==2):
        points = 3
    return points


def game_party(points, balance, username):
    money = 0
    pt = points
    magic_number = random.randint(0, 100)
    print("                          The MAGIC number has being choosen PLAY!!")
    for i in range(0, points):
        print("                    Total Points left : ", pt-i , "Points")
        print("Enter a number From 0 to 100")
        numbre_choisi = int(input())
        if(numbre_choisi<magic_number):
            print("failed!!...You are less than the Magic number try Again")
            continue
        elif(numbre_choisi>magic_number):
            print("failed!!... You are greater than the MAGIC number try again")
            continue
        else:
            print("SUCCESS!!!!!!!!!!!!!!!!. You found the magic number")
            money = money * 2 + 2000
            print(" Money Cumulated : ", money , "XAF || Points Left : ", pt-i, " Points")
            print("               Will you like to")
            print("                  1. Continue to play and try gaining more money")
            print("                  2. Stop here and collect your Gains")
            print("             N/B : If you continue and loss, you will loss all your funds")
            choice = int(input())
            if(choice == 1):
                magic_number = random.randint(0, 100)
                continue
            else:
                print("Congratulations you won : ", money , "XAF")
                balList = fg.fileread("balance.data")
                usList = fg.fileread("userList.data")
                balList[usList.index(username)]+=money
                fg.filewrite("balance.data", balList)  
                Menu.Menu(username, money+balance)
    print("GAME OVER, You lost every thing, points exhausted")
    Menu.Menu(username, balance)

def game_description(us, bal):
    print("                         GAME RULES  ")
    print("         1. When you launch a party, select a level between Easy, Medium, Hard, and Extreme")
    print("         2. You have 15, 10, 5 and 3 attempts respectively to find the magic number for Easy, Medium, Hard, Extreme")
    print("         3. When you succeed once, you can continue to play with your left points but if you fail you loose even the money you won already")
    print("         4. Any time you win your money gain is given by gain = (money*2 + 2000)XAF")
    print("         5. When your points reach 0, the party is over and your money is lost")
    print("         6. You win the party when you find the magic number in the range 0 to 100 and decide to stop thus collecting your points  ")
    Menu.Menu(us, bal)
    return
                
def menu(balance):
    print("            Current Balance : ", balance, "XAF")
    print("                            MENU")
    print("                        1. New Party")
    print("                        2. View Description and Rules")
    print(" Select what you wish to do")
    menuchoice = int(input())
    if(menuchoice == 1 ):
        game_party(level_select())
    elif(menuchoice == 2):
        game_description()
    else:
        exit(0)
    return


    
    
    
    



