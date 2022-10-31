# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 01:39:49 2022

@author: George
"""


def Register():
    print("Create your account")
    Username = input("Enter username: ")
    Password = input("Enter your password: ")
    return (Username,Password)


def Login():
    print("Login")
    Username=input("Username: ")
    Password=input("Password: ")
    return (Username,Password)


def start():
    print("                 ====================================================================")
    print("                 =                                                                  =")
    print("                 =                        MAGIC NUMBER                              =")
    print("                 =                                                                  =")
    print("                 =                       by CARTEL V1.0                             =")
    print("                 =                                                                  =")
    print("                 ====================================================================")
    print("What do you want to do?")
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    return int(input())