import cv2 
# image_paths=['../images/S1.jpg','../images/S2.jpg','../images/S3.jpg','../images/S5.jpg','../images/S6.jpg']
# image_paths=['../images/1Hill.JPG','../images/2Hill.JPG','../images/3Hill.JPG']
image_paths=['../images/1.jpg','../images/2.jpg','../images/3.jpg']
# initialized a list of images 
imgs = [] 

for i in range(len(image_paths)): 
	print(image_paths[i])
	imgs.append(cv2.imread(image_paths[i]))
	cv2.imshow(str(i),imgs[i]) 
	# imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
	# this is optional if your input images isn't too large 
	# you don't need to scale down the image 
	# in my case the input images are of dimensions 3000x1200 
	# and due to this the resultant image won't fit the screen 
	# scaling down the images 
# showing the original pictures 
# cv2.imshow('1',imgs[0]) 
# cv2.imshow('2',imgs[1]) 
# cv2.imshow('3',imgs[2]) 

stitchy=cv2.Stitcher.create(1) 
(dummy,output)=stitchy.stitch(imgs) 

if dummy != cv2.STITCHER_OK: 
# checking if the stitching procedure is successful 
# .stitch() function returns a true value if stitching is 
# done successfully 
	print("stitching ain't successful") 
else: 
	print('Your Panorama is ready!!!') 

# final output 
cv2.imshow('SCANS final result',output) 

stitchy=cv2.Stitcher.create(0) 
(dummy,output)=stitchy.stitch(imgs) 

if dummy != cv2.STITCHER_OK: 
# checking if the stitching procedure is successful 
# .stitch() function returns a true value if stitching is 
# done successfully 
	print("stitching ain't successful") 
else: 
	print('Your Panorama is ready!!!') 

# final output 
cv2.imshow('PANORAMA final result',output) 

cv2.waitKey(0)
