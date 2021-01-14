import cv2
import numpy as np

img_bgr = cv2.imread(r"C:\Users\mayan\PycharmProjects\valorantMusicPlayer\Images\buyphase.png")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread(r'C:\Users\mayan\PycharmProjects\valorantMusicPlayer\templates\buyphase.png', 0)
w, h = template.shape[::-1]

print(type(img_gray))
print(type(template))

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pos in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pos, (pos[0]+w, pos[1]+h), (255,0,0), 2)
    break

cv2.imshow('output', img_bgr)
cv2.waitKey(0)