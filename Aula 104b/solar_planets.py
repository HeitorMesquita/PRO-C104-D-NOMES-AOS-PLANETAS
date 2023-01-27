import cv2

Image = cv2.imread("solar-system.jpg")

cv2.putText(Image,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(Image,"Mercurio",(110,180),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Terra",(300,270),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Marte",(400,270),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Jupiter",(500,90),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Saturno",(720,110),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Urano",(950,130),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))
cv2.putText(Image,"Netuno",(1080,130),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255))


cv2.imshow("resultado",Image)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",Image)
