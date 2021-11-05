import cv2

img_color = cv2.imread('bus.jpg')
print(type(img_color))
cap = cv2.VideoCapture('bus.jpg')
assert cap.isOpened(), f'Failed to open {s}'
print(max(cap.get(cv2.CAP_PROP_FPS) % 100, 0) or 30.0)
print(max(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), 0) or float('inf'))
ret, frame = cap.read()
print(type(frame))
cv2.imshow('color', frame)
cv2.waitKey(0)