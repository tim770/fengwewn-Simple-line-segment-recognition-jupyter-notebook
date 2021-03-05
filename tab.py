import os 
import cv2
from matplotlib import pyplot as plt
import numpy as np  
import math
import time

cap = cv2.VideoCapture(0)
currentWB = cap.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U) 
cap.set(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, currentWB)

while(True):
    try :
        t1 = time.time()
        ret,frame = cap. read()
        scr =  frame.copy()
        brightLAB = cv2.cvtColor(scr, cv2.COLOR_BGR2LAB)
        red = brightLAB[..., 1]
        ret,red_1 = cv2.threshold (red, 130, 255, 0)
        white_mask = cv2.bitwise_and(scr,scr, mask=red)
        gray= cv2.cvtColor(white_mask,cv2.COLOR_BGR2GRAY)

        gn=gray.ravel()
        gh=np.zeros(256,dtype =int) 

        for i in range (len(gn)):
            gh[gn[i]]+=1
        img= np.zeros((512,512,3),np.uint8)

        for i in range(256):
            cv2.line(img,(i*2,2000),(i*2,2000-gh[i]),(255,0,0),2)
    
        qu = np.zeros(9)
        qc = math.ceil(256/30)

        for i in range(qc):
            qu[i-1] = gh[(i-1)*30:((i-1)*30+30)].sum()
        max_2=int(0)
        wei=int(0)
        for i in range (qc):
            if qu[i] >max_2:
                max_2=qu[i]
                wei=i
    
        max_1=int(0)
        wei_1=int(0)
        for i in range(qc):
            if(qu[i] > max_1)and(i != wei):
                max_1=qu[i]
                wei_1=i
        if abs(wei_1-wei)>2:
            print("stranger,none")
    #break (realtime)

        elif len(qu) > int(wei + 2):
            cv2.imshow('',gray)
            ret,thresh1 = cv2.threshold(gray,(wei + 2)*30,255,4)
            cv2.imshow('thresh1-f',thresh1)
            cv2.imshow('img',img)
            cv2.imshow('red-tong',red)
            cv2.imshow('red-qie',red_1)

        t2 = time.time()
        print('time elapsed: ' + str(round(t2-t1, 2)) + ' seconds')
    


        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release
            cv2.destroyAllWindows()
            break

    except ValueError:
        print(error)

