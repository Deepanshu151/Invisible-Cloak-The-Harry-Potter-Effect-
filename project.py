import cv2
import numpy as np
import time

# Start video capture
cap = cv2.VideoCapture(0)  # 0 = default camera

time.sleep(2)  # wait for the camera to warm up
background = 0

# Capture background frame (make sure cloak is not visible)
for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)

# Process video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = np.flip(frame, axis=1)  # mirror effect
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define color range for red cloak in HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = mask1 + mask2
    
    # Refine the mask (remove noise)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8))
    
    # Invert mask to get rest of the area
    mask_inv = cv2.bitwise_not(mask)
    
    # Segment out cloak from frame
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Replace cloak area with background
    res2 = cv2.bitwise_and(background, background, mask=mask)
    
    # Final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("Invisible Cloak", final_output)
    
    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
