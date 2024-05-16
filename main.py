# This is a program about authentication checker in which the user can sign up or log in to their account and delete their account
# Owner: May Thu Htun (T0333024)

import string  # to use 'string.ascii_uppercase'
import os  # to interact with os


# checking whether numbers are present and how many numbers are there in a password
def numberPW(password):
    count = 0
    for i in numbers:
        for c in password:
            if c == i:
                count += 1
    return count


# checking if there is a upper-case alphabet in a password
def capPW(password):
    found = False
    for letter in capitalLetter:
        if password.find(letter) > -1:
            found = True
    return found


# checking whether special symbols are present and how many of them are there in a password
def symbolsPW(password):
    count = 0
    for i in symbols:
        for c in password:
            if c == i:
                count += 1
    return count


# create a file to store user information
def createFile():
    try:
        if (os.path.isfile("userDetails.txt")):
            print("Let's GO!")
        else:
            print("Let's G0!")
            file = open("userDetails.txt", "x")
            file.close()
    except:
        print("File cannot be written in your device.")


# to ask users input
def signUp():
    users = []
    Loop = True
    while Loop == True:
        username = input("\nEnter your username: ")
        username = "'" + username + "'"
        file = open("userDetails.txt", "r")
        data = file.read()
        # checking if the username is taken or not
        if data.find(username) != -1:
            print("This username is taken. Try another one!")
            Loop = True
        else:
            Loop = False
            users.append(username)
            print("\nCreate your password. Password must contain 11 characters(3 nums, 2 symbols, 1 capital letter)")
            loop = True  # looping until user password meet the password requirements
            while loop == True:
                password = input("Enter your password: ")
                if len(password) > 10:
                    if numberPW(password) > 2:
                        if capPW(password) == True:
                            if symbolsPW(password) > 1:
                                loop = False
                                users.append(password)
                                name = input(
                                    "\nEnter your full name: ")  # after setting the password asking the user personal information
                                print("")
                                users.append(name)

                                # user input age must be a number which is larger than 1 and try to catch error if the user input is not an integer or less than 1
                                again = True
                                while again == True:
                                    try:
                                        age = int(input("Enter your age: "))
                                        if age < 1:
                                            print("The age you have entered does not exist in human world!")
                                            again = True
                                        else:
                                            users.append(str(age))
                                            again = False
                                    except ValueError as e:
                                        print(e)
                                        print("Enter only numbers!!!")
                                        again = True

                                address = input("\nEnter your address: ")
                                print("")
                                users.append(address)

                                # user phone number must be 10 digit number and try to catch error if the user input is not an integer or less than 10 numbers or more than 10 numbers
                                repeat = True
                                while repeat == True:
                                    try:
                                        mobile = int(
                                            input("Enter your phone number: NOTE! Do not include 0 at the front! "))
                                        mobile = str(mobile)
                                        if len(mobile) != 10:
                                            print(
                                                "The phone number you have entered is invalid! Phone number should have 10 digit.")
                                            repeat = True
                                        else:
                                            users.append(mobile)
                                            repeat = False
                                    except ValueError as e:
                                        print(e)
                                        print("Enter only numbers!!!")
                                        repeat = True

                                nationality = input("\nEnter your nationality: ")
                                users.append(nationality)

                                # making user enter their email until the email include "@gmail.com"
                                email = input("\nEnter your email address: ")
                                while email.find("@") == -1:
                                    print("That email in invalid!")
                                    email = input("Enter your email address: ")
                                else:
                                    users.append(email)

                            else:
                                print("Password must contain at least 2 symbols!")
                                loop = True
                        else:
                            print("Password must contain at least 1 upper-case(capital) letter!")
                            loop = True
                    else:
                        print("Password must contain at least 3 numbers!")
                        loop = True
                else:
                    print("Password must contain at least 11 characters!")
                    loop = True

    return users


# to check the login process (whether the username matches with the password)
def logIn():
    global username
    Loop = True
    while Loop == True:
        file = open("userDetails.txt", "r")
        data = file.read()
        username = input("\nEnter your username: ")
        username = "'" + username + "'"
        if data.find(username) == -1:
            print("Try again!")
        else:
            index = data.index(username)
            password = input("Enter your password: ")
            password = "'" + password + "'"
            if data.find(password) == -1:
                print("Try again!")
            else:
                index2 = data.index(password)
                if index2 == (index + len(
                        username) + 3):  # using index to check if the username and password is for one person.
                    print("Login Successfully")
                    uList = readToFile()
                    delAcc(uList)
                    Loop = False
                else:
                    print("Your username and password does not match!")
                    Loop = True
                    file.close()


# to read the file
def readToFile():
    file = open("userDetails.txt", "r")
    content = file.readlines()
    file.close()
    return content


# deleting the user account by confirming their username
def delAcc(content):
    delete = []
    dele = input("\nDo you want to delete your account? Type 'y' to delete ")
    if dele == "y":
        usernameDel = input("Enter your username: ")
        usernameDel = "'" + usernameDel + "'"
        if usernameDel != username:
            print("Sorry! Your username is incorrect!")
        elif usernameDel == username:
            print("Your account has been deleted.")
            file = open("userDetails.txt", "w")
            for number, line in enumerate(content):
                word = str(line)
                if (word.find(usernameDel)) != -1:
                    delete.append(number)

                if number not in delete:
                    file.writelines(line)


# to write a file
def writeFile(users):
    file = open("userDetails.txt", "a")
    file.writelines(users)
    file.write("\n")
    file.close()


# main
createFile()
# code modified from https://www.educative.io/answers/what-is-the-asciiuppercase-constant-in-python
# date accessed 1 November 2022
capitalLetter = string.ascii_uppercase  # allows to use all the upper case letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '£', '$', '%', '^', '&', '*', '(', ')', '€', '#']
loop = True
while loop == True:
    choose = input("Type L to login or S to signup ").upper()
    if choose == "L":
        logIn()
        loop = False
    elif choose == "S":
        data = str(signUp())
        writeFile(data)
        loop = False
    else:
        loop = True
