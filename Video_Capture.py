# Video capture
import cv2

vid = cv2.VideoCapture(0)
# If you want to capture from preloaded video just give the name of video at the place of '0'
# Also change 'True' to 'vid.isOpened()'
while (True):

    ret, frame = vid.read()  # Each frame capture

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting each fram into B/W format

    cv2.imshow("Frame", gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Checking for keypress for quitting
        print("Key Pressed...Exitting")
        break
# The windows will only be closed when key 'q' is pressed. Closing from 'Close' icon will not work 
vid.release() # Never forget to release the frame
cv2.destroyAllWindows()

