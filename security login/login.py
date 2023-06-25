import os
import customtkinter as ctk
import tkinter as tk
app = ctk.CTk()
app.title("CTkButton")
button = customtkinter.CTkButton(
    app, text="CTkButton", command=button_event)


def button_event():
    print("button pressed")
