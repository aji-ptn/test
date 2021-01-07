import cv2

nama_img = "C:\\Users\\Aji Pamungkas\\PycharmProjects\\pythonProject1\\Resources/BP_Africo.jpg"
img = cv2.imread(nama_img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(img,90,90)
_,thresh = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)

cv2.imshow("thresh",thresh)
cv2.imshow("gray",gray)
cv2.imshow("canny",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
