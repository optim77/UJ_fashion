from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from utils.image import FashionPoseImage
import cv2
from PIL import Image, ImageTk
#BIBLIOTEKA DAJĄCA WIĘCEJ MOŻLIWOŚCI EDYTOWANIA GUI NIŻ PODSTAWOWY TKINTER
import customtkinter
from base import run_outfit


#USTAWIENIE ZMIENNYCH GLOBALNYCH
BG_COLOR = 'black'
BUTTON_COLOR = 'blue'
HOVER_BUTTON_COLOR = 'blue'
FONT = 'Comic Sans MS'
BIG_FONT_SIZE = 25
SMALL_FONT_SIZE = 14


# FUNKCJA INICJALIZUJĄCA FRAME ZE SKELTON MODE
def load_skeleton(outfit):
    frame = customtkinter.CTkFrame(master=window)
    label = Label(master=frame, text='alfa')
    img = Image.fromarray(run_outfit(outfit))
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(20, load_skeleton())

    # run_skeleton()
    frame.pack()
    label.pack()


# FUNKCJA URUCHAMIANA PO WYBORZE WEBCAM WYŚWIETLAJĄCA MOŻLIWE MODELE
def options():
    frame = customtkinter.CTkFrame(master=window)
    frame_label = customtkinter.CTkLabel(frame,
                                         text='Choose outfit',
                                         text_font=(FONT, BIG_FONT_SIZE, 'bold'))


    # TWORZENIE PRZYCISKU ODPOWIEDZIALNEGO ZA WYŚWIETLENIE SZKIELETU
    skeleton = customtkinter.CTkButton(frame,
                                       text='Skeleton',
                                       text_font=(FONT, BIG_FONT_SIZE),
                                       command=lambda: load_skeleton(outfit='Skeleton'))

    astrounat = customtkinter.CTkButton(frame,
                                       text='Astronaut',
                                       text_font=(FONT, BIG_FONT_SIZE),
                                       command=lambda: load_skeleton(outfit='Astronaut'))

    jacket = customtkinter.CTkButton(frame,
                                        text='Jacket',
                                        text_font=(FONT, BIG_FONT_SIZE),
                                        command=lambda: load_skeleton(outfit='Jacket'))
    frame_label.pack()
    skeleton.pack()
    astrounat.pack(pady=10)
    jacket.pack(pady=10)
    frame.pack(side='top', fill='both', expand=True)
    frame_label.pack()
    webcam_frame = False


# FUNKCJA LADUJĄCA ZDJĘCIA Z PLIKU ODNOSZĄCA SIĘ DO DZIEDZICZONEJ KLASY W PLIKU images.py,
# FashionPoseImage DZIEDZICZY PO FashionPose W PLIKU app.py
def load_image():
    path = fd.askopenfilename(title='Open File')
    image = cv2.imread(path)
    img = FashionPoseImage(path, outfit='Skeleton')
    img = Image.fromarray(img)
    print(img)
    label = Label(master=window, image=img)
    label.image = img
    label.configure(image=img)
    label.pack()


# DOMYŚLNE USTAWIENIA customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# LADOWANIE KAMERY
window = customtkinter.CTk()
# window.geometry('1920x1080')
# USTAWIANIE KOLORU TLA
window.configure(bg=BG_COLOR)
# USTAWIANIE WYŚWIETLANIA NA CALY EKRAN
window.attributes('-fullscreen', True)

greetings = customtkinter.CTkLabel(window, text='Hello in FashionApp',
                                   padx=10,
                                   pady=50,
                                   text_font=(FONT, BIG_FONT_SIZE, 'bold'))

descriptions = customtkinter.CTkLabel(window, text='With this app you can try '
                                                   'on different costumes from different eras.',
                                      height=50,
                                      padx=10,
                                      pady=20,
                                      text_font=(FONT, SMALL_FONT_SIZE))

webcam = customtkinter.CTkButton(window,
                                 text='Start by webcam',
                                 text_font=(FONT, BIG_FONT_SIZE),
                                 command=lambda: options())

loadImage = customtkinter.CTkButton(window,
                                    text='Start by loading image',
                                    text_font=(FONT, BIG_FONT_SIZE),
                                    command=load_image)


exit = customtkinter.CTkButton(window,
                               text='Exit',
                               command=lambda: window.quit(),
                               text_font=(FONT, BIG_FONT_SIZE),
                               )


exit.place(relx=10, rely=100)
greetings.pack()
descriptions.pack()
webcam.pack(pady=30)
loadImage.pack(pady=30)
exit.pack(pady=30)
window.mainloop()

