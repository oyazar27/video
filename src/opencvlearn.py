# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('/Users/omer/NetBeansProjects/video/images/messi5.jpg',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.imwrite('/Users/omer/NetBeansProjects/video/images/messigray.png',img)
