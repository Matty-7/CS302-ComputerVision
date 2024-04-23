from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by OpenCV. You can process both videos and images.')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='KNN')
args = parser.parse_args()

## [create]
#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
    # history=50, varThreshold =16, detectShadows=False
    #backSub.setNMixtures(3)
else:
    backSub = cv.createBackgroundSubtractorKNN()
    # history=50, dist2Threshold=30, detectShadows=False
## [create]

## [capture]
# Change the input for the camera here; you might need to change the index to 1 or higher if 0 is not the front camera.
capture = cv.VideoCapture(1)  # Trying with index 1, assuming it's the front camera
if not capture.isOpened():
    print('Unable to open camera')
    exit(0)
## [capture]

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    ## [apply]
    # Update the background model
    fgMask = backSub.apply(frame)
    # learning rate
    ## [apply]

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel, iterations=2)
    fgMask = cv.dilate(fgMask, None, iterations=3)

    fgImg = cv.bitwise_and(frame, frame, mask=fgMask)

    ## [display_frame_number]
    # Get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    ## [display_frame_number]

    ## [show]
    # Show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Image', fgImg)
    ## [show]

    keyboard = cv.waitKey(30)
    if keyboard == ord('q') or keyboard == 27:
        break

# When everything done, release the capture
capture.release()
cv.destroyAllWindows()

