<h1>Otsu Method</h1>

<h2>Description</h2>
Project consists of a simple Python script that uses cv2 instead of OpenCV to perform Otsu Method operations, with the goal of getting a better understanding of image processing.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>CV2</b>
- <b>Terminal</b>

<h2>Environments Used </h2>

- <b>MacOS</b>

<h2>Program Results:</h2>

<p align="center">
Image 1: <br/>
<img src="https://imgur.com/IUOAWp2.png" height="60%" width="60%" alt="Hough Transform Results"/>
</p>
I started by loading the two images using open cv imread command, cv2.cvtColor is then applied over the image input with applied parameters to convert the image into grayscale. I then applied Otsu thresholding with an extra flag in binary thresholding for both images, giving me the result above.
<br />
<br />
<p align="center">
Image 2:  <br/>
<img src="https://imgur.com/4Jl8HP6.png" height="60%" width="60%" alt="Hough Transform Results"/>
</p>
I used both cv2 and pyplot to create my output, starting by loading the image as usual, and gray scaling it. I then generated regions, and thresholds using threshold_multiotsu, and np.digitize commands. I added a histogram to display the thresholds along with the original image with the results onto one plot with 3 axes.
<br />
<br />
<p align="center">
Image 3: <br/>
<img src="https://imgur.com/wPFvfOi.png" height="60%" width="60%" alt="Hough Transform Results"/>
</p>
For mean shift I loaded the image, added a filter to reduce the noise, and flattened the image before applying mean shift to it. I then printed the amount of segments generated and it came out to be 13. I got the average color of each segment in order to cast the labeled image into the corresponding average color, giving me the result above.
