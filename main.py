import numpy as np
import cv2 as cv
from sklearn.cluster import MeanShift, estimate_bandwidth         
import numpy as np     

########### TWO CLASS ############

image1 = cv.imread('OTSU2class-edge_L-150x150.png')
image2 = cv.imread('OTSU2class-andreas_L-150x150.png') 

#convert the image to grayscale 
img1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY) 
img2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)  
# applying Otsu thresholding       
ret1, thresh1 = cv.threshold(img1, 120, 255, cv.THRESH_BINARY + 
                                            cv.THRESH_OTSU) 
ret2, thresh2 = cv.threshold(img2, 120, 255, cv.THRESH_BINARY + 
                                            cv.THRESH_OTSU)     
    
########### MULTI CLASS ############

import matplotlib.pyplot as plt    
from skimage.filters import threshold_multiotsu

image = cv.imread('OTSU Multiple Class-S01-150x150.png')
multi_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# MultiOtsu will return multiple thresholds
thresholds = threshold_multiotsu(multi_image)
# Generate regions
regions = np.digitize(multi_image, bins=thresholds)
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

# Plotting the original image.
ax[0].imshow(multi_image, cmap='gray')
ax[0].set_title('Original')
ax[0].axis('off')

# Plotting the histogram and the two thresholds obtained from multi-Otsu.
ax[1].hist(multi_image.ravel(), bins=255)
ax[1].set_title('Histogram')
for thresh in thresholds:
    ax[1].axvline(thresh, color='r')

# Plotting the Multi Otsu result.
ax[2].imshow(regions, cmap='jet')
ax[2].set_title('Multi-Otsu result')
ax[2].axis('off')

plt.subplots_adjust()

########### MEANSHIFT ############

img = cv.imread('meanshift.png')

# filter to reduce noise
img = cv.medianBlur(img, 3)

# flatten the image
flat_image = img.reshape((-1,3))
flat_image = np.float32(flat_image)

# meanshift
band_width = estimate_bandwidth(flat_image, quantile=.06, n_samples=3000)
ms = MeanShift(bandwidth=band_width, max_iter=800, bin_seeding=True)
ms.fit(flat_image)
labeled=ms.labels_


# number of segments
segments = np.unique(labeled)
print('Number of segments: ', segments.shape[0])

# average color of each segment
total = np.zeros((segments.shape[0], 3), dtype=float)
count = np.zeros(total.shape, dtype=float)
for i, label in enumerate(labeled):
    total[label] = total[label] + flat_image[i]
    count[label] += 1
avg = total/count
avg = np.uint8(avg)

# cast labeled image into corresponding average color
res = avg[labeled]
result = res.reshape((img.shape))

# show the result
cv.imshow('Otsu Threshold Edge', thresh1)
cv.imshow('Otsu Threshold Andreas', thresh2)
cv.imshow('Meanshift',result)            
plt.show() 

cv.waitKey(0)
cv.destroyAllWindows()