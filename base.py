import cv2
from utils.app import FashionPose
import tkinter as tk
from PIL import Image, ImageTk
show_webcam = True


def run_outfit(outfit):
    # Initialize ExorcistFace class
    draw_skeleton = FashionPose(show_webcam, outfit_type='Skeleton')
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    draw_skeleton.outfit_type = outfit

    while cap.isOpened():

        # Read frame
        ret, frame = cap.read()

        if not ret:
            continue

        # Flip the image horizontally
        frame = cv2.flip(frame, 1)

        ret, skeleton_image = draw_skeleton(frame)

        if not ret:
            continue

        cv2.imshow("Exorcist face", skeleton_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
