# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
# from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
import pymysql
from src.em import camclick

def enf(fn,vid):




	knownEncodings = []
	knownNames = []
	name="name"
	# loop over the image paths


	image = fn
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detect the (x, y)-coordnates of the bounding boxes
	# corresponding to each face in the input image
	boxes = face_recognition.face_locations(rgb,
		model='hog')

	# compute the facial embedding for the face
	encodings = face_recognition.face_encodings(rgb, boxes)

	# loop over the encodings
	for encoding in encodings:
		# add each encoding + name to our set of known names and
		# encodings
		knownEncodings.append(encoding)
		knownNames.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f = open('faces.pickles', "wb")
	f.write(pickle.dumps(data))
	f.close()
	con = pymysql.connect(host='localhost', port=3306, user='root', password='Root_root1', db='pupil_emotion')
	cmd = con.cursor()

	cmd.execute("SELECT * FROM student;")
	s=cmd.fetchall()
	print(s,"=================")
	data = pickle.loads(open('faces.pickles', "rb").read())
	for r in s:

		print(r[7],"============")
		image = cv2.imread("./static/staffpic/"+r[6])
		print(image,"=======================================================================img")
		# print(image)
		h, w, ch = image.shape
		print(ch)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


		print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb,
												model='hog')
		encodings = face_recognition.face_encodings(rgb, boxes)

		# initialize the list of names for each face detected
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],
													 encoding,tolerance=0.4)


			if True in matches:

				emo=camclick(fn)
				rating=5
				if emo=='surprise':
					rating=4
				elif emo=='neutral':
					rating=2.5
				elif emo=='fear' or emo=='sad':
					rating=2
				elif emo=='angry':
					rating=0.5
				elif emo=='disgust':
					rating=0

				cmd.execute("insert into emotion values(null,'"+str(vid)+"','"+emo+"','"+str(rating)+"','1')")
				con.commit()
				return "ok"

	return "na"

