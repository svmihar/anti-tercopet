import cv2
import numpy as np
import argparse
import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO)
logger = logging.getLogger(__name__)


cap=cv2.VideoCapture(0)

def main(thresholdarea: int, delaytime: int):
    while(True):
        ret1,frame1= cap.read()
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
        ret2,frame2=cap.read()
        cv2.waitKey(delaytime)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

        deltaframe=cv2.absdiff(gray1,gray2)
        cv2.imshow('delta',deltaframe)
        threshold = cv2.threshold(deltaframe, 25, 255, cv2.THRESH_BINARY)[1]
        threshold = cv2.dilate(threshold,np.ones((3,3), np.uint8),iterations=2)
        cv2.imshow('threshold',threshold)
        _,countour,heirarchy = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in countour:
            if cv2.contourArea(i) <thresholdarea :
                text = "isi"
                logger.info(cv2.contourArea(i))
                continue
            (x, y, w, h) = cv2.boundingRect(i)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame2, f'Status: {text}', (10,40), cv2.FONT_HERSHEY_SIMPLEX, 2.1, (0, 0, 255), 5)
        cv2.imshow('window',frame2)
        text = "kosong"
        if cv2.waitKey(20) == ord('q'):
          break
    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=500)
    parser.add_argument('--delay', type=int, default=100)
    args = vars(parser.parse_args())
    main(**args)
