desc = '''Script to collect images

usage: python data_collection.py <label_name> <number_of_samples>

This script will automatically collect given number of samples and store them in
a directory of the provided label name

press s to start/pause collecting data
press q to quit the window

'''
import cv2
import os
import sys

try: 
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])
except:
    print("Invalid Arguments")
    print(desc)
    exit(-1)

img_path = r'E:/Kaggle/Project_1/Rock_Paper_Scissors/data'
class_path = os.path.join(img_path, label_name)

try: 
    os.mkdir(class_path)
except FileExistsError:
    print(f'{class_path} already exists')
    print("New images will be saved along with the existing ones")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

start = False
count = 0

if not cap.isOpened():
    print("Camera is not working")
    exit()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        continue

    if count == num_samples:
        break

    if start:
        save_path = os.path.join(class_path, f'{label_name}_{count+1}.jpg')
        cv2.imwrite(save_path, frame)
        count+=1

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f"Collecting {count}", (5, 50), font, 0.7, (0,0,0), 2, cv2.LINE_AA)
    cv2.imshow("Images", frame)

    if cv2.waitKey(15) == ord('s'):
        start = not start

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

