import random
import string
import sqlite3
import hashlib
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image
import os
from Database import *
from  Credentials import *
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
vault = {}

class TLW(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x500")


class PasswordManager(ctk.CTk):
    width = 1000
    height = 650

    def __init__(self):
        super().__init__()

        # background image
        self.bg_image = ctk.CTkImage(Image.open("vault2.png"), size=(200, 200))
        # initialize the login screen window
        self.title("Password Manager")
        self.geometry(f"{self.width}x{self.height}")

        # creating login system
        self.frame = ctk.CTkFrame(self, corner_radius=0)
        self.frame.pack(padx=20, pady=20)
        self.label = ctk.CTkLabel(self.frame, text="*", image=self.bg_image)
        self.label.pack(padx=20, pady=20)
        self.username = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username.pack(padx=20, pady=20)
        self.password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password.pack(padx=20, pady=20)
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login_event, width=200)
        self.login_button.pack(padx=20, pady=20)
        self.create_account = ctk.CTkButton(self.frame, text="Create Account", command=self.create_acc, width=200)
        self.create_account.pack(padx=20, pady=20)
        self.app_exit = ctk.CTkButton(self.frame, text="Exit", command=self.quit, width=200)
        self.app_exit.pack(padx=20, pady=20)
        self.rm_checkbox = ctk.CTkCheckBox(self.frame, text="Remember Me")
        self.rm_checkbox.pack(padx=20, pady=20)

    def create_acc(self):
        self.acc_button = TLW(self)
        self.acc_label = ctk.CTkLabel(self.acc_button, text="Create a Username and Password.")
        self.acc_label.pack(side="top", padx=20, pady=20)
        self.u_entry = ctk.CTkEntry(master=self.acc_button, placeholder_text="Username", width=120, height=25,
                                    border_width=2, corner_radius=10)
        self.u_entry.pack(side="top", padx=20, pady=20)
        self.p_entry = ctk.CTkEntry(master=self.acc_button, placeholder_text="Password", show="*", width=120, height=25,
                                    border_width=2, corner_radius=10)
        self.p_entry.pack(side="top", padx=20, pady=20)

        self.button = ctk.CTkButton(master=self.acc_button, text="Create Account", command=self.user_insert)
        self.button.pack(padx=20, pady=20)

    # creating password vault menu
    def vault(self):
        # Password Credentials
        self.grid_rowconfigure((0, 3), weight=1)
        self.grid_columnconfigure((0, 3), weight=1)
        ##self.PC_frame = ctk.CTkFrame(self, corner_radius=0, command=self.show_creds)
        ##self.PC_frame.grid(row=0, column=0, rowspan=2, columnspan=4, padx=20, pady=(20, 0),
                                            ##sticky="nsew")
        self.PC_Label = ctk.CTkLabel(master=self, text="Credentials", fg_color="transparent")
        self.PC_Label.grid(row=0, column=0, padx=20, pady=(20, 0))
        self.PC_User = ctk.CTkLabel(master=self, text="Username", fg_color="transparent")
        self.PC_Label.grid(row=1, column=1, padx=20, pady=(20, 0))

        ##self.passwordvault_credentials.insert("0", self.password)

        # Button Options
        self.cimput = ctk.CTkButton(master=self, text="Add Entry", command=self.add_e)
        self.cimput.grid(row=3, column=0, padx=20, pady=20)
        self.dimput = ctk.CTkButton(master=self, text="Delete Entry")
        self.dimput.grid(row=3, column=1, padx=20, pady=20)
        self.passwordvault_logout = ctk.CTkButton(master=self, text="Logout", command=self.logout_event)
        self.passwordvault_logout.grid(row=3, column=3, padx=20, pady=20)
        self.passwordvault_generate = ctk.CTkButton(master=self, text="Generate Password",
                                                    command=self.generate_p)
        self.passwordvault_generate.grid(row=3, column=2, padx=20, pady=20)

    # creating a login event that allows user io input credentials and access the vault
    # NEEDS WORK
    def login_event(self):
        username = self.username.get()
        password = self.password.get()

        print("Username: ", self.username.get(), "Password: ", self.password.get())
        if check_user_acc(username, password):
            ##self.frame.destroy()
            ##self.vault()
            print("Login Successful")
        else:
            print("Try Again...")


    # creating an event that logs out the user
    # NEEDS WORK
    def logout_event(self):
        self.quit()

    def generate_p(self):
        self.window_entry = ctk.CTkInputDialog(text="Enter the # of characters for your password", title="Input")
        var = int(self.window_entry.get_input())

        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        random.shuffle(characters)

        self.password = []

        for x in range(var):
            self.password.append(random.choice(characters))

        random.shuffle(self.password)  # randomizes a password

        self.password = "".join(self.password)
        print("\n" + self.password + "\n")
        self.passwordvault_credentials.insert("0", self.password)

    def add_e(self):
        self.adbutton = TLW(self)
        self.label = ctk.CTkLabel(self.adbutton, text="Add the entries below")
        self.label.pack(side="top", padx=20, pady=20)
        self.u_entry = ctk.CTkEntry(master=self.adbutton, placeholder_text="Username", width=120, height=25,
                                    border_width=2, corner_radius=10)
        self.u_entry.pack(side="top", padx=20, pady=20)
        self.p_entry = ctk.CTkEntry(master=self.adbutton, placeholder_text="Password", width=120, height=25,
                                    border_width=2, corner_radius=10)
        self.p_entry.pack(side="top", padx=20, pady=20)
        self.w_entry = ctk.CTkEntry(master=self.adbutton, placeholder_text="Website", width=120, height=25,
                                    border_width=2, corner_radius=10)
        self.w_entry.pack(side="top", padx=20, pady=20)

        self.button = ctk.CTkButton(master=self.adbutton, text="ADD", command=self.cred_insert)
        self.button.pack(padx=20, pady=20)

    # NEEDS WORK
    def cred_insert(self):
        con = sq.connect('vault.db')
        c = con.cursor()
        username = self.u_entry.get()
        password = self.p_entry.get()
        website = self.w_entry.get()
        print("Username: ", username, "Password: ", password, "Website: ", website)

        insertion = """INSERT INTO vault(username,password,website)
        VALUES(?,?,?)"""
        c.execute(insertion, (username, password, website))
        con.commit()

    def user_insert(self):
        username = self.u_entry.get()
        password = self.p_entry.get()
        website = "example.com"
        print("Username: ", username, "Password: ", password)
        create_user_account(username, password)

        ##self.message = ctk.C

    # Needs Work
    def show_creds(self):
        '''
        con = sq.connect('vault.db')
        c = con.cursor()
        c.execute("SELECT * FROM vault")
        i = c.fetchall()
        return i
        '''



if __name__ == "__main__":
    app = PasswordManager()
    app.mainloop()
