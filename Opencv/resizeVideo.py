import cv2 as cv
#reading video
def rescaleFrame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension= (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture= cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized= rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
