from PIL import ImageGrab, Image
import cv2
import numpy as np

screenshot = ImageGrab.grab()
img = Image.open(r"C:\Users\mayan\PycharmProjects\valorantMusicPlayer\Images\death.png")

w, h = img.size
print(f"{w} {h}")

tx = 134
ty = 851
bx = 273
by = 874

imgCrop = img.crop((tx, ty, bx, by))
imgCrop.save("templates/death.png")

imgCrop.show()

