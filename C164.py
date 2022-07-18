from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()
root.geometry("500x500")
root.title("PLANET ENCYCLOPEDIA")
root.configure(background="plum2")
mercury=ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
earth=ImageTk.PhotoImage(Image.open("earth.jpg"))
planets=["Mercury","Venus","Earth"]
selectedval=StringVar()
dropdown=ttk.Combobox(root,values=planets,textvariable=selectedval)
dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)
label_heading=Label(root,text="Planets",font=("Roman"),bg="plum2")
label_heading.place(relx=0.2,rely=0.1,anchor=CENTER)
label_planet_name=Label(root,font=("Roman",18,"bold"),bg="plum2")
label_planet_name.place(relx=0.5,rely=0.25,anchor=CENTER)
label_gravity_radius=Label(root,font=("Roman"),bg="plum2")
label_gravity_radius.place(relx=0.5,rely=0.8,anchor=CENTER)
label_planet_info=Label(root,font=("Roman",10,"bold"),bg="plum2",wraplength=200)
label_planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)
label_image=Label(root,bg="orchid4",highlightthickness=5,borderwidth=2,relief=SOLID)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)
def planetinfo():
    planetname=selectedval.get()
    if planetname=="Mercury":
        label_planet_name["text"]="Mercury"
        label_image["image"]=mercury
        label_gravity_radius["text"]="Gravity:3.7 m/s2 \n Radius:2439.7km"
        label_planet_info["text"]="Mercury is the smallest planet in the Solar System and the closest to the Sun. Its orbit around the Sun takes 87.97 Earth days, the shortest of all the Sun's planets"
    elif planetname=="Venus":
        label_planet_name["text"]="Venus"
        label_image["image"]=venus
        label_gravity_radius["text"]="Gravity:8.87m/s2 \n Radius:6051.8km"
        label_planet_info["text"]="Venus is the second planet from the Sun and is named after the Roman goddess of love and beauty. As the brightest natural object in Earth's night sky after the Moon, Venus can cast shadows and can be visible to the naked eye in broad daylight."
    elif planetname=="Earth":
        label_planet_name["text"]="Earth"
        label_image["image"]=earth
        label_gravity_radius["text"]="Gravity:9.8m/s2 \n Radius:6371km"
        label_planet_info["text"]="Earth is the third planet from the Sun and the only astronomical object known to harbor life. While large volumes of water can be found throughout the Solar System, only Earth sustains liquid surface water. About 71% of Earth's surface is made up of the ocean, dwarfing Earth's polar ice, lakes, and rivers"
button_show=Button(root,command=planetinfo,text="Show Info")
button_show.place(relx=0.5,rely=0.18,anchor=CENTER)
root.mainloop()