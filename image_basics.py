
#1 Print OpenCV Version
'''
import cv2

def main():
	print(cv2.__version__)


if __name__ == "__main__":
	main()

'''
#2 Reading and Displaying Images - Method 1
'''
import cv2

def main():
	
	imgpath = "/home/ss51210/Pictures/Sha2nk's Image/IoT Images/img9.jpg"
	img = cv2.imread(imgpath)

	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()

'''
#3 Reading and Displaying Images - Method 2
'''

import cv2

def main():
	
	imgpath = "/home/ss51210/Pictures/Sha2nk's Image/IoT Images/kaa_img.png"
	img = cv2.imread(imgpath)

	cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyWindow('Lena')


if __name__ == "__main__":
	main()


'''
#4 Image reading modes and Writing an image to disc
'''

import cv2

def main():
    
    imgpath = "/home/ss51210/Pictures/Sha2nk's Image/IoT Images/img9.jpg"
    #img = cv2.imread(imgpath, 0)  #Grayscale Mode
    img = cv2.imread(imgpath, 1)  #Standard Color Mode
    #img = cv2.imread(imgpath,-1)  #Standard Color Mode with channels
    print(img)

    
    outpath = "/home/ss51210/Pictures/Sha2nk's Image/snapshots/img9.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
	main()	

'''
#5 Images, Numbers, and NumPy
  #Internally OpenCV relays information in Blue Green Red Format.


import cv2
import numpy as np

def main():
    
    imgpath = "/home/ss51210/Pictures/Sha2nk's Image/IoT Images/kaa_img.png"
    img1 = cv2.imread(imgpath, 0)
    
    print(img1) #print entire image in numbers
    print(type(img1)) #data type of entire image representation in numbers
    print(img1.dtype) #data type of each element 
    
    print(img1.shape) #resolution of image
    print(img1.ndim) #number of dimensions
    print(img1.size)
    
#    cv2.imshow('Lena', img1)
#    cv2.waitKey(0)
#    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
	main()


