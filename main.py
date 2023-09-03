import customtkinter
import tkinter

# Sets the display mode of the GUI to system. 
# If the user's system is in dark mode, the PokerEV window will be in dark mode. Likewise for light mode.
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# Represents the main window of the PokerEV application
pokerev_root = customtkinter.CTk()

# Sets the default 
pokerev_root.geometry("1280x720")