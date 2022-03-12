import time
from os import system
from db import db

my_cursor = db.cursor()


class Registration:
    def __init__(self):
        self.new_login = None
        self.new_password = None
        self.name = None
        self.login_ = None
        self.password = None
        self.welcome()

    def welcome(self):
        system("clear")
        choice = input("Welcome to my app.\nChoose one of the below: \n[1] Register\n[2] Login\nPress any other "
                       "key to exit\n")
        self.register() if choice == "1" else self.login() if choice == "2" else exit()
    #
    def register(self):
        self.name = input("Enter your name: ")
        self.login_ = input("Enter your login: ")
        while self.checkLogin():
            self.login_ = input("This user already exists. Enter your login: ")
        self.password = input("Enter your password: ")
        while not self.checkPassword(self.password):
            self.password = input("Your password is too weak. Please try another one: ")
        my_cursor.execute(f"insert into users values(null,'{self.name}','{self.login_}','{self.password}')")
        db.commit()
        print("You registered successfully!")
        choice = input("Enter 1 to log in or enter any key to exit")
        self.login() if choice == "1" else exit()

    def update(self):
        system("clear")
        choice = input(
            "[1] Update password\n[2] Update login\n[3] Logout\n[4] Delete account\n Press any other key to exit\n")
        self.update_password() if choice == "1" else self.update_login() if choice == "2" else self.log_out() if \
            choice == "3" else self.delete_account() if choice == "4" else exit()

    def login(self):
        system("clear")
        self.update_things()
        if self.checkUser():
            print("You logged in successfully!")
            self.update()
        else:
            system("clear")
            print("No such user!")
            time.sleep(5)
            self.welcome()

    def update_things(self):
        system("clear")
        self.login_ = input("Enter your login: ")
        self.password = input("Enter your password: ")

    # def update_login(self):
    #     self.update_things()
    #     if self.checkUser():
    #         self.new_login = input("Enter your new login: ")
    #         while not self.checkLogin():
    #             self.new_login = input("Already exists. Try another one: ")
    #         my_cursor.execute(f"update users set login='{self.new_login}' where login='{self.login_}' and "
    #                           f"password='{self.password}'")
    #         db.commit()
    #     else:
    #         print("No such user!")
    #         self.update()
    #
    @staticmethod
    def checkPassword(password):
        return len(password) >= 6

    def checkLogin(self):
        my_cursor.execute(f"select * from users where login='{self.login_}'")
        return not not my_cursor.fetchall()

    def checkUser(self):
        my_cursor.execute(f"select * from users where login='{self.login_}' and password='{self.password}'")
        return not not my_cursor.fetchall()

    # def delete_account(self):
    #     self.update_things()
    #     if self.checkUser():
    #         my_cursor.execute(f"delete from users where login='{self.login_}' and password='{self.password}'")
    #         db.commit()
    #     else:
    #         print("No such user!")
    #         self.update()


user = Registration()