import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import FD

def capture_face_contrast():
    while True:
        print("\nChoose an option:")
        print("1️⃣ Capture face from camera")
        print("2️⃣ Upload existing image")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "2":
            root = tk.Tk()
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )

            root = tk.Tk()
            root.withdraw()                    # create/withdraw root once

            while True:
                file_path = filedialog.askopenfilename(
                    title="Select an Image",
                    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")],
                    parent=root
                )
                if not file_path:
                    print("❌ No file selected. Exiting.")
                    break

                frame = cv2.imread(file_path)
                if frame is None:
                    print("❌ Could not read image. Try another.")
                    continue


                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

                for (x, y, w, h) in faces:
                    face_roi = gray[y:y+h, x:x+w]
                    contrast = np.std(face_roi)
                    if contrast < 30:
                        color, status = (0, 0, 255), "Low"
                    elif contrast < 60:
                        color, status = (0, 255, 255), "Medium"
                    else:
                        color, status = (0, 255, 0), "High"

                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
                    cv2.putText(frame, f"Contrast: {contrast:.1f} ({status})",
                                (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

                cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
                cv2.imshow("Image", frame)
                print("Press SPACE to select another file, ESC to exit.")

                k = cv2.waitKey(0) & 0xFF   # blocks until keypress while window has focus
                cv2.destroyWindow("Image")  # remove window before next dialog/loop

                if k == 27:                 # ESC -> exit
                    print("Exiting (ESC).")
                    break
            
                elif k == 32:               # SPACE -> loop again (select another file)
                    print("Select another image (SPACE pressed).")
                    continue
                else:
                    print(f"Exiting (key {k} pressed).")
                    break
            break
        if choice == "1":
             FD.capture_face_contrast_mediapipe("C:/Users/manin/Desktop/face_contrast.jpg")
             break          
        else:
            print("choose 1 or 2 only.")
            continue
    
        
capture_face_contrast()



