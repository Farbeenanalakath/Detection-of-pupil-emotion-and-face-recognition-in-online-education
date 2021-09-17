import numpy as np
import cv2
from  src.encode_faces import enf
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import time
from tkinter import *
from tkinter import messagebox
cap = cv2.VideoCapture(0)
WORD = re.compile(r'\w+')

from collections import Counter
import math
#-----------------------------
#face expression recognizer initialization
import pymysql
con=pymysql.connect(host='localhost', port=3306,user='root',password='',db='facialattendance')
cmd=con.cursor()
fn=''





while(True):
	try:
		ret, img = cap.read()
		# img=cv2.imread(fn)
		print(ret)

		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		print(len(faces))
		# for (x,y,w,h) in faces:
		# 	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image


		emolist=[]
		cv2.imshow("Frame",img)
		if len(faces)>0:

			fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
			print(fn)
			cv2.imwrite("static/pic/"+fn,img)
			enf("static/pic/"+fn)



		if cv2.waitKey(1) & 0xFF == 27:

			break
	except Exception as e:
		print(e)
		pass

