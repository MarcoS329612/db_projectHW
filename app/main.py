# app/main.py

import tkinter as tk
from app.gui.login import LoginWindow

def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
