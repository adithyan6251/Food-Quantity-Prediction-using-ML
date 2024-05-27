# important libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from matplotlib import image
from tkinter import filedialog
import tkinter
import tkinter.messagebox
import customtkinter
from infer import get_inference

leftover = []

days = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
# modes and themes
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# ----------------------------------- constants,global variables and images -----------------------------------------

WIDTH = 1200
HEIGHT = 600

global day1
global day3

global time1
global time3

logo = customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/cooking.ico"),size=(100,100))
appamEgg = customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/appam egg.jfif"),size=(200,200))
bread = customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/bread butter jam.jfif"),size=(200,200))
cib = customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/cb.jfif"),size=(200,200))
mainlogo =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/waste logoBgless.png"),size=(300,300))
gheerice =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/ghee rice.jfif"),size=(200,200))
meals =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/meals.jfif"),size=(200,200))
upma =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/upma.jfif"),size=(200,200))
puttu =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/putt&kadala.jfif"),size=(200,200))
dosa =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/dosa.jpeg"),size=(200,200))
idli =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/udli sambar.jfif"),size=(200,200))
kanji =customtkinter.CTkImage(light_image=Image.open("C:/Users/adith/OneDrive/Desktop/Project/food_quantity_prediction/images/kanji.jfif"),size=(200,200))

#------------------------------------ LAYERS --------------------------------------------------------------------

# main window
main = customtkinter.CTk()
main.title("EMPTY BIN")
main.geometry(f"{WIDTH}x{HEIGHT}")
main.state('zoomed')
main.protocol("WM_DELETE_WINDOW",main.destroy)

# Heading of the app
Heading= customtkinter.CTkLabel(master=main,text="EMPTY BIN",font=("Times New Roman",24,"bold"),width=100,height =50,fg_color=("white", "#50C878"),corner_radius=6)  
Heading.grid(row=0, column=1, columnspan = 1,pady=20, padx=20,sticky='nwe')

# sidepanel to update new values
sidepanel = customtkinter.CTkFrame(master=main,width=180,corner_radius=6)
sidepanel.grid(row=0, column=0,rowspan=2,sticky="ns",padx=20,pady=20)

# inputpanel to take inputs
inputpanel = customtkinter.CTkFrame(master=main)
inputpanel.grid(row=1, column=1,sticky="nwe", padx=20, pady=10)

# designpanel to put a symbol
design= customtkinter.CTkLabel(master=main,width=300,height=300,corner_radius=6,text=" ",image=mainlogo)  
design.grid(row=0, column=2,rowspan=2,pady=20, padx=20,sticky='nw')

# display to show our data
display= customtkinter.CTkFrame(master=main,width=200,height=330,corner_radius=6,fg_color=("white", "gray38"))  
display.grid(row=3, column=0, columnspan = 4,rowspan=1,pady=20, padx=20,sticky='nwe')

displaypanel= customtkinter.CTkLabel(master=main,font=("Times New Roman",14,"bold"),text="DISPLAY PANEL",width=20,fg_color=("white", "gray38"),corner_radius=6)  
displaypanel.grid(row=2, column=0, columnspan = 4,pady=10, padx=20,sticky='we')

#--------------------------------------------- FUNCTIONS------------------------------------------------------------

# function to clear everthing
def CLEAR():

   global day1
   global day3

   global time1
   global time3
  
   for widgets in display.winfo_children():
      widgets.destroy()
   
   day1=''
   time1=''
   
   day3=''
   time3=''

   DAY1.set("Day")
   DAY3.set("Day")

   TIME1.set("Time")
   TIME3.set("Time")
    
   veg.delete(0,END)
   veg.insert(END,"Vegitarian count")

   Nveg.delete(0,END)
   Nveg.insert(END,"Non Vegitarian count")

# function to get date for update
def WRITE1(choice):
   global day1 
   day1 = choice 

# function to get time for update
def WRITE2(choice):
   global time1
   time1 = choice

# function to get date for prediction
def WRITE3(choice):
   global day3 
   day3 = choice 

# function to get time for prediction
def WRITE4(choice):
   global time3
   time3 = choice

# function to update
def UPDATE():
   global day1
   global time1

   window = customtkinter.CTkToplevel(main)
   window.title("UPDATE")
   window.geometry("500x300")

   display1 = customtkinter.CTkFrame(master=window,corner_radius=6,width=460,height=300)
   display1.pack(padx=20,pady=20,fill=BOTH)

   if(day1=="Monday"):
      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Monday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         puttu1= customtkinter.CTkLabel(master=display1,text="Puttu",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         puttu1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         puttu2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         puttu2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         kadala1= customtkinter.CTkLabel(master=display1,text="Kadala",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         kadala1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         kadala2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         kadala2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):
         view= customtkinter.CTkLabel(master=display1,text="Monday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         sambar1= customtkinter.CTkLabel(master=display1,text="Sambar",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         sambar1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         sambar2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         sambar2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         aviyal1= customtkinter.CTkLabel(master=display1,text='Aviyal',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         aviyal1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         aviyal2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         aviyal2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Monday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         biriyani1= customtkinter.CTkLabel(master=display1,text="Biriyani",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         biriyani1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         biriyani2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         biriyani2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

      
         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=2, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')
   
   elif(day1=="Tuesday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Tuesday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         uppma1= customtkinter.CTkLabel(master=display1,text="Uppma",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         uppma1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         uppma2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         uppma2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):
         view= customtkinter.CTkLabel(master=display1,text="Tuesday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         sambar1= customtkinter.CTkLabel(master=display1,text="Parip curry",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         sambar1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         sambar2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         sambar2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         egg1= customtkinter.CTkLabel(master=display1,text='Egg',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         egg1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         egg2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         egg2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Tuesday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         idiyappam1= customtkinter.CTkLabel(master=display1,text="Idiyappam",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         idiyappam1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         idiyappam2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         idiyappam2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         greenpeas1= customtkinter.CTkLabel(master=display1,text="Greenpeas",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         greenpeas1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         greenpeas2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         greenpeas2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

   elif(day1=="Wednesday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Wednesday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         dosa1= customtkinter.CTkLabel(master=display1,text="Dosa",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         dosa1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         dosa2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         dosa2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         chutny1= customtkinter.CTkLabel(master=display1,text="Chutny",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         chutny1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         chutny2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         chutny2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):

         view= customtkinter.CTkLabel(master=display1,text="Wednesday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         sambar1= customtkinter.CTkLabel(master=display1,text="Sambar",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         sambar1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         sambar2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         sambar2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         beans1= customtkinter.CTkLabel(master=display1,text='Cabbage thoran',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         beans1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         beans2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         beans2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Wednesday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         gheerice1= customtkinter.CTkLabel(master=display1,text="Ghee rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         gheerice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         gheerice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         gheerice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         chickenCurry1= customtkinter.CTkLabel(master=display1,text="Chicken curry",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         chickenCurry1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         chickenCurry2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         chickenCurry2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

   elif(day1=="Thursday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Thursday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         dosa1= customtkinter.CTkLabel(master=display1,text="Idli",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         dosa1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         dosa2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         dosa2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         chutny1= customtkinter.CTkLabel(master=display1,text="Chutny",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         chutny1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         chutny2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         chutny2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):

         view= customtkinter.CTkLabel(master=display1,text="Thursday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         sambar1= customtkinter.CTkLabel(master=display1,text="Sambar",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         sambar1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         sambar2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         sambar2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         beans1= customtkinter.CTkLabel(master=display1,text='Beans',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         beans1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         beans2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         beans2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Thursday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         appam1= customtkinter.CTkLabel(master=display1,text="Appam",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         appam1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         appam2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         appam2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         eggCurry1= customtkinter.CTkLabel(master=display1,text="egg curry",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         eggCurry1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         eggCurry2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         eggCurry2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

   elif(day1=="Friday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Friday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         uppma1= customtkinter.CTkLabel(master=display1,text="Uppma",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         uppma1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         uppma2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         uppma2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):

         view= customtkinter.CTkLabel(master=display1,text="Friday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         chickenFry1= customtkinter.CTkLabel(master=display1,text="Chicken Fry",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         chickenFry1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         chickenFry2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         chickenFry2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         beans1= customtkinter.CTkLabel(master=display1,text='betroot',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         beans1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         beans2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         beans2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Friday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         puttu1= customtkinter.CTkLabel(master=display1,text="Puttu",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         puttu1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         puttu2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         puttu2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         kadala1= customtkinter.CTkLabel(master=display1,text="Kadala",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         kadala1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         kadala2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         kadala2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

   elif(day1=="Saturday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Friday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         idiyappam1= customtkinter.CTkLabel(master=display1,text="Idiyappam",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         idiyappam1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         idiyappam2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         idiyappam2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         greenpeas1= customtkinter.CTkLabel(master=display1,text="Greenpeas",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         greenpeas1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         greenpeas2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         greenpeas2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')
         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):

         view= customtkinter.CTkLabel(master=display1,text="Friday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         chickenCurry1= customtkinter.CTkLabel(master=display1,text="Fish curry",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         chickenCurry1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         chickenCurry2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         chickenCurry2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=4, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Friday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         biriyani1= customtkinter.CTkLabel(master=display1,text="Biriyani",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         biriyani1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         biriyani2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         biriyani2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

      
         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=2, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

   elif(day1=="Sunday"):

      if(time1=="Breakfast"):
         view= customtkinter.CTkLabel(master=display1,text="Sunday : Breakfast",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         bread1= customtkinter.CTkLabel(master=display1,text="Bread",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         bread1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         bread2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         bread2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         butter1= customtkinter.CTkLabel(master=display1,text="Butter",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         butter1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         butter2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         butter2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=3, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      elif(time1=="Lunch"):

         view= customtkinter.CTkLabel(master=display1,text="Sunday : Lunch",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

         rice1= customtkinter.CTkLabel(master=display1,text="Rice",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         rice1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         rice2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         rice2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         sambar1= customtkinter.CTkLabel(master=display1,text="Sambar",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         sambar1.grid(row=2, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         sambar2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         sambar2.grid(row=2, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         beans1= customtkinter.CTkLabel(master=display1,text='Beans',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         beans1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         beans2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         beans2.grid(row=3, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         aviyal1= customtkinter.CTkLabel(master=display1,text='Aviyal',width=100,fg_color=("white", "gray38"),corner_radius=6)  
         aviyal1.grid(row=3, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         aviyal2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         aviyal2.grid(row=4, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=5, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

      else:
         view= customtkinter.CTkLabel(master=display1,text="Sunday : Dinner",width=300,fg_color=("white", "gray38"),corner_radius=6)  
         view.grid(row=0, column=0, columnspan=2,pady=20, padx=20)

         riceSoup1= customtkinter.CTkLabel(master=display1,text="Rice Soup",width=100,fg_color=("white", "gray38"),corner_radius=6)  
         riceSoup1.grid(row=1, column=0, columnspan=1,pady=10, padx=10,sticky='w')
         riceSoup2= customtkinter.CTkEntry(master=display1,placeholder_text="leftover",width=250)
         riceSoup2.grid(row=1, column=1,columnspan =1 ,pady=10, padx=10,sticky='e')

         enter= customtkinter.CTkButton(master=display1,text="ENTER")
         enter.grid(row=2, column=0,columnspan =2 ,pady=10, padx=10,sticky='e')

def ENTER():

    global day3
    global time3

    num = int(veg.get()) + int(Nveg.get())

    
    p=get_inference(days[day3],num)

    pre1= customtkinter.CTkLabel(master=display,text="PREDICTION",font=("Times",24,"bold"),width=100,corner_radius=6)  
    pre1.grid(row=0, column=1, columnspan=1,pady=10, padx=10,sticky='ne')

    if(day3=="Monday"):
      if(time3=="Breakfast"):
         
         imgputtu= customtkinter.CTkLabel(master=display,text=" ",image=puttu,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgputtu.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         puttu3= customtkinter.CTkLabel(master=display,text=f"Puttu {p[0]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         puttu3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         kadala3= customtkinter.CTkLabel(master=display,text=f"Kadala {p[1]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         kadala3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"sambar {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         aviyal3= customtkinter.CTkLabel(master=display,text=f"aviyal {p[11]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         aviyal3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:
         imgbiri= customtkinter.CTkLabel(master=display,text=" ",image=cib,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgbiri.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         biriyani3= customtkinter.CTkLabel(master=display,text=f"biriyani {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         biriyani3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
    elif(day3=="Tuesday"):
      if(time3=="Breakfast"):
         
         imguppuma= customtkinter.CTkLabel(master=display,text=" ",image=upma,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imguppuma.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         upma3= customtkinter.CTkLabel(master=display,text=f"upma {p[4]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         upma3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"sambar {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         egg3= customtkinter.CTkLabel(master=display,text=f"Egg Thoran {int(p[10])} qty",font=("Sanserif",20),width=100,corner_radius=6)  
         egg3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgappam= customtkinter.CTkLabel(master=display,text=" ",image=appamEgg,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgappam.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         Iddiyappam3= customtkinter.CTkLabel(master=display,text=f"Iddiyappam {int(p[13])} qty",font=("Sanserif",20),width=100,corner_radius=6)  
         Iddiyappam3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         greenpeas3= customtkinter.CTkLabel(master=display,text=f"greenpeas {p[14]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         greenpeas3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')      

    elif(day3=="Wednesday"):
      if(time3=="Breakfast"):
         
         imguppuma= customtkinter.CTkLabel(master=display,text=" ",image=dosa,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imguppuma.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         dosa3= customtkinter.CTkLabel(master=display,text=f"dosa {p[2]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         dosa3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chutney3= customtkinter.CTkLabel(master=display,text=f"chutney {p[3]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chutney3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"parrip curry {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         beans3= customtkinter.CTkLabel(master=display,text=f"Cabbage thoran {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         beans3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgghee= customtkinter.CTkLabel(master=display,text=" ",image=gheerice,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgghee.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         gheerice3= customtkinter.CTkLabel(master=display,text=f"ghee rice {p[15]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         gheerice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chickencurry3= customtkinter.CTkLabel(master=display,text=f"chicken curry {p[16]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chickencurry3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')    

    elif(day3=="Thursday"):
      if(time3=="Breakfast"):
         
         imguppuma= customtkinter.CTkLabel(master=display,text=" ",image=dosa,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imguppuma.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         dosa3= customtkinter.CTkLabel(master=display,text=f"dosa {p[2]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         dosa3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chutney3= customtkinter.CTkLabel(master=display,text=f"chutney {p[3]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chutney3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"parrip curry {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         beans3= customtkinter.CTkLabel(master=display,text=f"Cabbage thoran {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         beans3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgghee= customtkinter.CTkLabel(master=display,text=" ",image=kanji,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgghee.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         gheerice3= customtkinter.CTkLabel(master=display,text=f"Rice Soup {p[19]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         gheerice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chickencurry3= customtkinter.CTkLabel(master=display,text=f"Beans {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chickencurry3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe') 

    elif(day3=="Friday"):
      if(time3=="Breakfast"):
         
         imguppuma= customtkinter.CTkLabel(master=display,text=" ",image=idli,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imguppuma.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         dosa3= customtkinter.CTkLabel(master=display,text=f"Idli {p[2]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         dosa3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chutney3= customtkinter.CTkLabel(master=display,text=f"chutney {p[3]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chutney3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"parrip curry {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         beans3= customtkinter.CTkLabel(master=display,text=f"Cabbage thoran {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         beans3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgghee= customtkinter.CTkLabel(master=display,text=" ",image=gheerice,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgghee.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         gheerice3= customtkinter.CTkLabel(master=display,text=f"ghee rice {p[15]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         gheerice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chickencurry3= customtkinter.CTkLabel(master=display,text=f"chicken curry {p[16]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chickencurry3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe') 

    elif(day3=="Saturday"):
      if(time3=="Breakfast"):
         
         imgputtu= customtkinter.CTkLabel(master=display,text=" ",image=puttu,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgputtu.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         puttu3= customtkinter.CTkLabel(master=display,text=f"Puttu {p[0]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         puttu3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         kadala3= customtkinter.CTkLabel(master=display,text=f"Kadala {p[1]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         kadala3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"parrip curry {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         beans3= customtkinter.CTkLabel(master=display,text=f"Cabbage thoran {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         beans3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgputtu= customtkinter.CTkLabel(master=display,text=" ",image=puttu,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgputtu.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         puttu3= customtkinter.CTkLabel(master=display,text=f"Puttu {p[0]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         puttu3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         kadala3= customtkinter.CTkLabel(master=display,text=f"Kadala {p[1]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         kadala3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
    elif(day3=="Sunday"):
      if(time3=="Breakfast"):
         
         imguppuma= customtkinter.CTkLabel(master=display,text=" ",image=dosa,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imguppuma.grid(row=0, column=0, rowspan=3,pady=10, padx=10,sticky='w')

         dosa3= customtkinter.CTkLabel(master=display,text=f"dosa {p[2]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         dosa3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         chutney3= customtkinter.CTkLabel(master=display,text=f"chutney {p[3]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         chutney3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

      elif(time3=="Lunch"):
         imgmeals= customtkinter.CTkLabel(master=display,text=" ",image=meals,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgmeals.grid(row=0, column=0, rowspan=4,pady=10, padx=10,sticky='w')

         rice3= customtkinter.CTkLabel(master=display,text=f"Rice {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         rice3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
         
         sambar3= customtkinter.CTkLabel(master=display,text=f"parrip curry {p[8]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         sambar3.grid(row=2, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')

         beans3= customtkinter.CTkLabel(master=display,text=f"Cabbage thoran {p[20]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         beans3.grid(row=3, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')
      else:

         imgbiri= customtkinter.CTkLabel(master=display,text=" ",image=cib,width=200,fg_color=("white", "gray38"),corner_radius=6)  
         imgbiri.grid(row=0, column=0, rowspan=2,pady=10, padx=10,sticky='w')

         biriyani3= customtkinter.CTkLabel(master=display,text=f"biriyani {p[7]} kg",font=("Sanserif",20),width=100,corner_radius=6)  
         biriyani3.grid(row=1, column=1, columnspan=1,pady=10, padx=10,sticky='nwe')  
#---------------------------------------------------sidepanel --------------------------------------------------------

# sidepanelHeading
logoDisplay= customtkinter.CTkLabel(master=sidepanel,image=logo,width=20,corner_radius=6,text=" ")  
logoDisplay.grid(row=0, column=0, pady=10, padx=20,sticky='we')

sidepanelHeading= customtkinter.CTkLabel(master=sidepanel,font=("Times New Roman",14,"bold"),text="UPDATE PANEL",width=20,fg_color=("white", "gray38"),corner_radius=6)  
sidepanelHeading.grid(row=1, column=0, pady=10, padx=20,sticky='we')

# variables for getting day and time
day2 = customtkinter.StringVar(value="Day")
time2 = customtkinter.StringVar(value="Time") 

# combobox for day in sidepanel
DAY1 = customtkinter.CTkComboBox(master=sidepanel,values=["Day", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],command=WRITE1,variable=day2)
DAY1.grid(row=2,column=0,columnspan =1, pady=10, padx=20, sticky="we")

# combobox for time in sidepanel
TIME1 = customtkinter.CTkComboBox(master=sidepanel,values=["Time", "Breakfast", "Lunch", "Dinner"],command=WRITE2,variable=time2)
TIME1.grid(row=3,column=0,columnspan =1, pady=10, padx=20, sticky="we")

update = customtkinter.CTkButton(master=sidepanel,text="UPDATE",command=UPDATE)
update.grid(row=4, column=0, pady=10, padx=20, sticky="we")

# ------------------------------------------------------ inputpanel ---------------------------------------------------------

# inputpanelHeading
inputpanelHeading = customtkinter.CTkLabel(master=inputpanel,text="INPUT PANEL",font=("Times New Roman",14,"bold"),height=10,corner_radius=6,fg_color=("white", "gray38"))
inputpanelHeading.grid(column=0, row=0,columnspan=2,sticky="nwe", padx=15, pady=15,ipadx=5, ipady=5)

# variables for getting day and time
day4 = customtkinter.StringVar(value="Day")
time4 = customtkinter.StringVar(value="Time") 

# combobox for day in inputpanel
DAY3 = customtkinter.CTkComboBox(master=inputpanel,values=["Day", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],command=WRITE3,variable=day4)
DAY3.grid(row=1,column=0,columnspan =1, pady=10, padx=20, sticky="we")

# combobox for time in inputpanel
TIME3 = customtkinter.CTkComboBox(master=inputpanel,values=["Time", "Breakfast", "Lunch", "Dinner"],command=WRITE4,variable=time4)
TIME3.grid(row=1,column=1,columnspan =1, pady=10, padx=20, sticky="we")

# taking count of vegiterians
veg= customtkinter.CTkEntry(master=inputpanel,width=300,placeholder_text="Vegitarian count")
veg.grid(row=2, column=0,columnspan =1, pady=20, padx=20,sticky='we')

# taking count of non vegiterians
Nveg= customtkinter.CTkEntry(master=inputpanel,width=300,placeholder_text="Non Vegitarian count")
Nveg.grid(row=2, column=1,columnspan =1 ,pady=20, padx=20,sticky='we')

veg.delete(0,END)
veg.insert(END,"Vegitarian count")
Nveg.delete(0,END)
Nveg.insert(END,"Non Vegitarian count")

# button to display
enter = customtkinter.CTkButton(master=inputpanel,text="ENTER",command=ENTER)
enter.grid(row=4, column=0, columnspan= 1,pady=10, padx=20, sticky="we")

# button to clear everything
enter = customtkinter.CTkButton(master=inputpanel,text="CLEAR",command=CLEAR)
enter.grid(row=4, column=1, columnspan= 1,pady=10, padx=20, sticky="we")

main.mainloop()
