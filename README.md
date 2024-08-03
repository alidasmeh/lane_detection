
# Lane Detection with CV lib

The aim of this project is creating a module to detect lane on the street only using images. For the Image Processing part, [OpenCV](https://opencv.org/) is used. 

-----

## How to run
Since this project includes some not common packages,  install all packages by running this command, first: 
```
pip install -r requirements.txt
```
You can see the packages inside ```requirements.text``` file. 

To run the python code by Terminal, go inside the project directory then run the code below: 
```
python lane_detection.py
```
By running this code, a new window will be opened to show you the result of the module.

-----
The project includes two video files. These are example used inside the code. You can choose the video you want by editing line #66.

-----

## Just test it to LEARN more 
### first
in function ```region_of_interest``` there is a commented code. Uncomment it, then comment the lines #26 to #32. You will see how different cv functions work to show the lines.

### second
in the line #66 change the input of ```cv2.VideoCapture``` function to ```road2.mp4```. Then run the code, the result will be so noisy. 
Then in line #8 try to change ```(5,5)``` to ```(9,9)``` to see how better it will work. This small change makes the image more blurry before further processes. 
