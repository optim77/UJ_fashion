import cv2
from utils.app import FashionPose
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
show_webcam = True
import mediapipe as mp
import matplotlib.pyplot as plt
from utils.background import load_background


def run_outfit(outfit):
    # Inicjalizacja klasy FashionPose
    draw_skeleton = FashionPose(show_webcam, outfit_type=outfit)
    # Inicjalizacja webcamu
    cap = cv2.VideoCapture(0)

    # wczytanie standardowego tła
    bg_image = cv2.imread('images/backgrounds/2.png')

    #ustawianie outfit w konstruktorze
    draw_skeleton.outfit_type = outfit

    while cap.isOpened():

        # Czytanie framów
        ret, frame = cap.read()

        # zmienianie tła po naciśnięciu przycisku
        keyboard = cv2.waitKey(1)
        bg_image = load_background(keyboard, bg_image)


        selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(1)
        # Ustawianie obrazu z kamery horyzontalnie
        frame = cv2.flip(frame, 1)

        # wczytywanie funkcji do rysowania ouffitu
        ret, skeleton_image = draw_skeleton(frame)

        # rysowanie tła
        results = selfie_segmentation.process(frame)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        output_image = np.where(condition, skeleton_image, bg_image)
        if not ret:
            continue

        # wyświetlanie outfitu oraz tła i czekanie na przycisk zamknięcia
        cv2.imshow("Exorcist face", output_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # zamykanie wszystkich okien po wyjściu z kamery
    cv2.destroyAllWindows()
