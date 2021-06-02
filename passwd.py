# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:52:51 2021

@author: cmulanshi
"""

def homePage():
    print("Welcome to the password tester program")
    print("Please enter your password for strength testing")
    print("************************************************")
    passwd = input(">")
    if lengthCheck(passwd) and charCheck(passwd) and upperCheck(passwd) and lowerCheck(passwd) and checkNum(passwd) == True:
        print(f"This Password {passwd} is very strong")
def lengthCheck(passwd):
    """Assumes passwd is a string, checks if length is greater than 10 
       Returns True if yes and None if false"""
    if len(passwd) < 10 or len(passwd) < 0:
        print("Invalid password length, your password is too short")
        homePage()
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
        homePage()
    else:
        return True
    
def upperCheck(passwd):
    """Assumes passwd is a string, checks if it contains an upper case character
       Returns True if yes and None if false"""
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    has_upper = False
    for c in passwd:
        if c in upperCase:
            #print(c)
            has_upper = True
            continue
    if has_upper == False:
        print("There are NO capital letters in your password")
        homePage()
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
        homePage()
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
        homePage()
    else:
        return True
            
homePage()
