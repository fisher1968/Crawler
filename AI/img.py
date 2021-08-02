import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from imgaug import augmenters as iaa
import imgaug as ia

# np.set_printoptions(threshold=np.inf)

img=cv2.imread(".\img\wenyao.jpg")

print('分辨率',img.shape[0],img.shape[1])
print('图片信息',img.shape)
plt.imshow(img)
plt.show()

# 读取灰度图

gray_img=cv2.imread(".\img\wenyao.jpg",cv2.IMREAD_GRAYSCALE)

print('灰度图分辨率',gray_img.shape[0],gray_img.shape[1])
print('灰度图图片信息',gray_img.shape)
plt.imshow(gray_img)
plt.show()

# 图片resize
img_400_300=cv2.resize(img,(400,300))

print('reszie图分辨率',img_400_300.shape[0],img_400_300.shape[1])
print('resize图图片信息',img_400_300.shape)
plt.imshow(img_400_300)
plt.show()


# 放射变换,放大1.2倍，然后平移
crop_m_image=np.array([[1.2,0,-50],[0,1.2,-100]],dtype=np.float32)
crop_img=cv2.warpAffine(img, crop_m_image, (300,200))

print('reszie图分辨率',crop_img.shape[0],crop_img.shape[1])
print('resize图图片信息',crop_img.shape)
plt.imshow(crop_img)
plt.show()



# cv2.imwrite(r".\img\wenyao_crop.jpg",crop_img)
# cv2.imwrite(r".\img\wenyao_resize.jpg",img_400_300)
# cv2.imwrite(r".\img\wenyao_gray.jpg",gray_img)
# cv2.imwrite(r".\img\wenyao_gray.jpg",gray_img)
# cv2.imwrite(r".\img\wenyao_resize.jpg",img_400_300)

img_girl_all = []

for filename in os.listdir(".\girl"):
    print(filename)
    print(len(img_girl_all))    
    img_girl = cv2.imread(".\girl"+"/"+filename)
    img_girl_all = img_girl_all.append(img_girl)
    print(len(img_girl_all))    

plt.show()


# img=cv2.imread(r".\girl\722ff2ffjw1ejlpyzzzu4j20rs15o18z.jpg")

# imgs=[img,img,img,img]

seq = iaa.Sequential([         #建立一个名为seq的实例，定义增强方法，用于增强
    iaa.Crop(px=(0, 30)),     #对图像进行crop操作，随机在距离边缘的0到160像素中选择crop范围
    iaa.Fliplr(0.5),   #对百分之五十的图像进行做左右翻转
    iaa.Flipud(0.2),   #对百分之二十的图像进行做左右翻转
    iaa.GaussianBlur((0, 1.0)),     #在模型上使用0均值1方差进行高斯模糊
    iaa.Affine(rotate=(-25, 25))
])

images_aug = seq.augment_images(img_girl_all)

ia.imshow(np.hstack(images_aug))

# print('reszie图分辨率',imgs.shape[0],img_girl_all.shape[1])
# print('resize图图片信息',imgs.shape)
# plt.imshow(images_aug)
# plt.show()