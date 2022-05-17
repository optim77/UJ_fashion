from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from utils.image import FashionPoseImage
import cv2
from PIL import Image, ImageTk
#BIBLIOTEKA DAJĄCA WIĘCEJ MOŻLIWOŚCI EDYTOWANIA GUI NIŻ PODSTAWOWY TKINTER
import customtkinter
from base import run_outfit

customtkinter.set_appearance_mode("dark")
#USTAWIENIE ZMIENNYCH GLOBALNYCH
BG_COLOR = 'black'
BUTTON_COLOR = 'blue'
HOVER_BUTTON_COLOR = 'blue'
FONT = 'Comic Sans MS'
BIG_FONT_SIZE = 25
SMALL_FONT_SIZE = 14


# FUNKCJA INICJALIZUJĄCA FRAME ZE SKELTON MODE
def load_skeleton(outfit, type):
    frame = customtkinter.CTkFrame(master=window)
    label = Label(frame, text='alfa')
    img = Image.fromarray(run_outfit(outfit, type))
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
    frame2 = customtkinter.CTkFrame(master=window)

    # TWORZENIE PRZYCISKU ODPOWIEDZIALNEGO ZA WYŚWIETLENIE SZKIELETU Z TLEM Z OBRAZKIEM
    frame_label_image = customtkinter.CTkLabel(frame,
                                         text='Choose outfit (Image)',
                                         text_font=(FONT, BIG_FONT_SIZE, 'bold'))
    frame_label_image.grid(column=0, row=0, sticky=W, padx=5, pady=5)

    skeleton_image = customtkinter.CTkButton(frame,
                                       text='Skeleton',
                                       text_font=(FONT, BIG_FONT_SIZE),
                                       command=lambda: load_skeleton(outfit='Skeleton', type='image'))

    astrounat_image = customtkinter.CTkButton(frame,
                                       text='Astronaut',
                                       text_font=(FONT, BIG_FONT_SIZE),
                                       command=lambda: load_skeleton(outfit='Astronaut', type='image'))

    jacket_image = customtkinter.CTkButton(frame,
                                        text='Jacket',
                                        text_font=(FONT, BIG_FONT_SIZE),
                                        command=lambda: load_skeleton(outfit='Jacket', type='image'))

    # TWORZENIE PRZYCISKU ODPOWIEDZIALNEGO ZA WYŚWIETLENIE SZKIELETU Z TLEM Z GIFEM
    frame_label_gif = customtkinter.CTkLabel(frame2,
                                               text='Choose outfit (GIF)',
                                               text_font=(FONT, BIG_FONT_SIZE, 'bold'))

    skeleton_gif = customtkinter.CTkButton(frame2,
                                             text='Skeleton',
                                             text_font=(FONT, BIG_FONT_SIZE),
                                             command=lambda: load_skeleton(outfit='Skeleton', type='gif'))

    astrounat_gif = customtkinter.CTkButton(frame2,
                                              text='Astronaut',
                                              text_font=(FONT, BIG_FONT_SIZE),
                                              command=lambda: load_skeleton(outfit='Astronaut', type='gif'))

    jacket_gif = customtkinter.CTkButton(frame2,
                                           text='Jacket',
                                           text_font=(FONT, BIG_FONT_SIZE),
                                           command=lambda: load_skeleton(outfit='Jacket', type='gif'))

    # WYSWIETLANIE LABELI
    frame_label_image.pack()
    frame_label_gif.pack(anchor=CENTER)
    # WYSWIETLANIE PRZYCISKOW IMAGE
    skeleton_image.pack(anchor=CENTER, pady=10)
    astrounat_image.pack(anchor=CENTER, pady=10)
    jacket_image.pack(anchor=CENTER, pady=10)
    #WYSWIETLANIE PRZYCISKOW GIF
    skeleton_gif.pack(anchor=CENTER, pady=10)
    astrounat_gif.pack(anchor=CENTER, pady=10)
    jacket_gif.pack(anchor=CENTER, pady=10)

    frame.pack(side='left', padx=100)
    frame2.pack(side='right', padx=100)
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
#loadImage.pack(pady=30)
exit.pack(pady=30)
window.mainloop()

