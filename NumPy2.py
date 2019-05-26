import numpy as np
from skimage import io
import scipy
import matplotlib.pyplot as plt


# numpy with image
pic = io.imread('pic.jpg')
print(pic)
print(pic.shape)
pltshow = plt.imshow(pic)
plt.title('actual pic')
plt.show()

pltshow1 = plt.imshow(pic[::-1])
plt.title('upside down pic')
plt.show()

pltshow2 = plt.imshow(pic[100:250,150:350])
plt.title('cropped pic')
plt.show()

x = np.sin(pic)
print(x)
x1 = np.max(pic)
x2 = np.min(pic)
x3 = np.mean(pic)
x4 = np.std(pic)
x5 = np.var(pic)
x6 = np.sum(pic)
x7 = np.prod(pic)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)


'''
from PIL import Image
jpgfile = Image. open("pic.jpg")
print(jpgfile. bits, jpgfile. size, jpgfile. format)
'''