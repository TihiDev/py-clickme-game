import tkinter as tk 

root = tk.Tk()
root.title("Kattintos jatek")
root.geometry("300x200")

score = 0 

def increase_score():
    global score 
    score += 1 
    label.config( text=f"Pontszam: {score}" )

def reset_score(): 
    global score 
    score = 0
    label.config( text=f"Pontszam: {score}" )

label = tk.Label( root, text="Pontszam: 0", font=("Arial", 20) )
label.pack( pady=20 )

button = tk.Button( root, text="Kattints ram!", font=("Arial", 14), command=increase_score )
buttonrst = tk.Button( root, text="Pontszam nullazas", font=("Arial", 14), command=reset_score )

button.pack()
buttonrst.pack()
root.mainloop()