# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:52:51 2021

@author: cmulanshi
"""
def menu():
    print("Enter passwd again!")
    passwd = input(">")
    if lengthCheck(passwd) and charCheck(passwd) and upperCheck(passwd) and lowerCheck(passwd) and checkNum(passwd) and dictCheck(passwd) == True:
        print(f"This Password {passwd} is very strong")
def home():
    print("Welcome to the password tester program")
    print("Please enter your password for strength testing")
    print("************************************************")
    passwd = input(">")
    if lengthCheck(passwd) and charCheck(passwd) and upperCheck(passwd) and lowerCheck(passwd) and checkNum(passwd) and dictCheck(passwd) == True:
        print(f"This Password {passwd} is very strong")
def lengthCheck(passwd):
    """Assumes passwd is a string, checks if length is greater than 10 
       Returns True if yes and None if false"""
    if len(passwd) < 10 or len(passwd) < 0:
        print("Invalid password length, your password is too short")
        print("Enter a password with atleast 10 characters.")
        menu()
        return False
    else:
        return True
        
def charCheck(passwd):
    """Assumes passwd is a string, checks if the passwd has a special character
       Returns True if yes and None if false"""
    has_char = False
    special = "!@#$%^&*()~?></\\"
    for c in passwd:
        if c in special:
            has_char = True
            continue
        
    if has_char == False:
        print("Your password has NO special characters e.g @#")
        menu()
        return False
    else:
        return True
    
def upperCheck(passwd):
    """Assumes passwd is a string, checks if it contains an upper case character
       Returns True if yes and None if false"""
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    has_upper = False
    for c in passwd:
        if c in upperCase:
            has_upper = True
            continue
    if has_upper == False:
        print("There are NO capital letters in your password")
        menu()
        return False
    else:
        return True
    
def lowerCheck(passwd):
    """Assumes passwd is a string, checks if the characters in passwd are lower case 
       Returns passwd if True and goes back to main menu when otherwise
    """
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    has_lower = False
    for c in passwd:
        if c in lowerCase:
            has_lower = True
            continue
    if has_lower == False:
        print("There are no lower case letters in your pass word")
        menu()
        return False
    else:
        return True
    
    
def checkNum(passwd):
    """Assumes passwd is a string, checks if it contains a number 
       Returns True if yes and None if false"""
    has_num = False
    for num in passwd:
        try:
            if type(int(num)) == int:
                has_num = True
            else:
                has_num == False
        except ValueError:
            continue
            
    if has_num == False:
        print("Your password must atleast contain a number")
        menu()
        return False
    else:
        return True

def dictCheck(passwd):
    """Assumes passwd is a string, checks to see if passwd in contained in dictionary data
       Returns False if yes and True if not """
    passList = list()
    fhandle = open("dict.txt",'r')
    for line in fhandle.readlines():
        passList.append(line.strip("\n"))
    if passwd in passList:
        print("WARNING!!Your password was found in a local dictionary")
        menu()
        return False
    else:
        fhandle2 = open("dict.txt",'a')
        if fhandle2.write(passwd + "\n"):
            pass
        return True


home()
