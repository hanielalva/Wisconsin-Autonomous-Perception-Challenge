# Wisconsin-Autonomous-Perception-Challenge
 This Python-based computer vision project utilizes OpenCV to create a perception algorithm that detects the boundaries of a straight path defined by cones captured by a vehicle-mounted camera. The 
 project's primary goal is to draw boundary lines representing the path on the image and save the result as a PNG file named "answer.png."

Methodology:
- Library Usage: The project relies on OpenCV (cv2) and NumPy as its primary libraries.
- Image Processing Steps:
    1) The project starts by loading the image and converting it into the HSV color space.
    2) A mask is applied to filter the image for the red color associated with the cones.
    3) The resulting image is converted to grayscale, followed by Gaussian blur to reduce noise and enhance edge detection.
    4) The Canny edge detection algorithm is employed to identify edges in the image.
    5) Since the cones are distributed on both halves of the image, it is split vertically into two halves for separate processing.
- Contour Analysis:
    1) For each half, the project identifies the contours of the red cones and calculates their centroids using a dedicated function.
    2) The custom function then draws lines on the original full image by connecting centroids of adjacent contours from each half, effectively outlining the path boundaries.
- Output Saving: The final modified image, complete with boundary lines, is saved as "answer.png."

Potential Improvements:
- The current implementation could benefit from improved filtering to exclusively detect cone contours. Currently, it may inadvertently pick up red color in the background, connecting lines to unrelated
  areas. Exploring algorithms that capture a wider spectrum of red while strictly filtering for cone shapes could enhance the results.
- The current implementation assumes two lines of cones arranged on each half of the screen. To make the code more adaptable to diverse images, research into recognizing patterns in cone arrangements
  would be necessary.

Personal Note (this is a bit long but it details my learning process, how I got to my implementation and what all I tried):
WOW, this was a super fun project to do! Coming into this chalenge, I had no prior experience in Computer Vision and I did not have any idea where to start. My first instinct after reading the write up
for the challenge was to throw the prompt at ChatGPT 3.5 and see what it came up with. It's explanation for how to attack this challenge seemed fairly logical. The code it gave used cv2 and numpy,
which I had no prior experience with. After getting it to successfully run without throwing an error it just drew a bunch of lines all over the output image. I spent a lot of time after that just watching 
YouTube videos on Computer Vision projects and OpenCV open source software tutorials. This helped a lot as it allowed me to grasp concepts that were essential to fine tuning the approach I had planned in 
my head. Initially, I did not take into consideration the cones' color and focused on just trying to filter for its shape and proximity which stumped me for a long time. I did that because I saw other red 
color in the photo apart from the cones and assumed that removed color filtering from the potential implementation but after coming back to the project after a nice break, I decided to mess around with the 
color. I first put red.png in an online RGB and HSV detector to look at the values for the red in the photo. After that, to save on time, I asked ChatGPT to estimate a range for the reds. I ended up 
just finetuning that range to get a filter of the image that was satisfying to me. This was a great milestone in the project because before that, I felt like I was getting no where. Now, I was stuck on 
how to draw lines from one cone contour to another. This seemed really complicated to me as the contours I had from my filter were not perfectly shaped like cones so the ideas relating to proximity, 
area and mid point did not make sense in my head nor worked out in the code I wrote or the code ChatGPT gave to me. I used ChatGPT a lot in this challenge and though its code never worked, it provided 
me with a great starting point to modify and improve the broken code it gave me. I struggle with writing code from scratch but finetuning and optimizing has always been a forte of mine. I posted 
about my line drawing issue on the WA Slack Challenge discussion chat for potential ideas from others (I had been scouring the Challenge discussion thread since the YouTube video part of my Personal 
Note). I got two suggestions. Pravin's made sense to me and I did try implementing that but I am new to numpy and I realized it would require a lot more leg work than Nevi's suggestion. Nevi's suggestion 
was already my main idea for how to solve the line drawing problem prior to posting but the way he framed his reponse to my post on the thread allowed me to think through and code my implementation in a 
more step by step manner. That is the long version of how I got to my implementation! El fin :D
