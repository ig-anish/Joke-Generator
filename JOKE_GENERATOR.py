import requests
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

#creating joke function
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    setup = data["setup"]
    punchline = data["punchline"]
    joke_label.config(text=f"{setup}\n\n{punchline}")


#creating the GUI window
window = tk.Tk()
window.title("Random Joke Generator")
window.geometry("700x400")
style = Style(theme="flatly")
window.style = style

#creating label widget
joke_label = tk.Label(text="Click the button to get a random joke!", font=("TkDefaultFont",20))
joke_label.place(relx=0.5, rely=0.5, anchor="center")

#creating button for joke
get_joke_button = ttk.Button(text=" Get Joke", command=get_joke)
get_joke_button.pack(pady=20)

window.mainloop()