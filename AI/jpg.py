import cv2
import numpy as np

img=cv2.imread("D:\workspace\AI\img\wenyao.jpg")
# 读取灰度图
gray_img=cv2.imread("D:\workspace\AI\img\wenyao.jpg",cv2.IMREAD_GRAYSCALE)
# 图片resize
img_400_300=cv2.resize(img,(400,300))

crop_m_image=np.array([[1.6,0,-150],[0,1.6,-240]],dtype=np.float32)

crop_img=cv2.warpAffine(img, crop_m_image, (300,200))

cv2.imwrite(r"D:\workspace\AI\img\wenyao_crop.jpg",crop_img)
cv2.imwrite(r"D:\workspace\AI\img\wenyao_resize.jpg",img_400_300)
cv2.imwrite(r"D:\workspace\AI\img\wenyao_gray.jpg",gray_img)
cv2.imwrite(r"D:\workspace\AI\img\wenyao_gray.jpg",gray_img)
cv2.imwrite(r"D:\workspace\AI\img\wenyao_resize.jpg",img_400_300)
cv2.imwrite(r"D:\workspace\AI\img\wenyao_gray.jpg",gray_img)

