import cv2
import numpy as np
import pyautogui as pnot

def record_screen(output_file, frame_rate, duration):

    screen_size = pnot.size()  # get screen size
    width, height = screen_size  # separate width and height
    fourcc = cv2.VideoWriter_fourcc(*"XVID") #filetype #'*' divides "XVID" into 4 separate characters X , V , I , D
    out = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

    for _ in range(duration * frame_rate):

        screenshot = pnot.screenshot()
        frame = np.array(screenshot)  # converting to numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #RGB --> BGR
        out.write(frame) #takes one image. many loops=many images

    out.release()
    print("recording complete")

if __name__ == "__main__": #This ensures that the script only runs when executed directly (not when imported into another script. Whenever you run a Python script, Python sets a special variable called __name__. If you run the script directly → __name__ becomes "__main__". If the script is imported → __name__ becomes the name of the file instead of "__main__".

    filename = input("enter filename: ")
    output_file = filename + ".mp4"  # set output file name
    frame_rate = 20  # set frame rate
    duration = int(input("Enter recording duration in seconds: "))  # get duration from user

    record_screen(output_file, frame_rate, duration)  # Call the function
