from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.config(background="lightblue")

mercury = ImageTk.PhotoImage(Image.open("mercuy.jpg"))
venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
earth = ImageTk.PhotoImage(Image.open("earth.jpg"))

label_planet = Label(root, text="Planet: ", bg="lightblue")
label_planet_name = Label(root, font=("courier",18,"bold"), bg="lightblue")
label_planet_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=FLAT)
label_planet_gravity = Label(root, font=("castellar"), bg="lightblue")
label_planet_info = Label(root, font=("courier",10,"bold"), bg="lightblue", wraplength=500)

planets = ["Mercury", "Venus", "Earth"]
planetaEscolhido = StringVar()
dropdown = ttk.Combobox(root, values= planets, textvariable= planetaEscolhido)

def planetinfo():
    planet = planetaEscolhido.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = mercury
        label_planet_gravity['text'] = "Gravity and radius - Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_planet_info['text'] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"

    elif planet == "Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = venus
        label_planet_gravity['text'] = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        label_planet_info['text'] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky"

    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = earth
        label_planet_gravity['text'] = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        label_planet_info['text'] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."

btn = Button(root, text="Show Planet Info", command=planetinfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()