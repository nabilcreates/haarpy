# Documentation
> Read more on Haar Cascade here: https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html

## Usage: `python3 main.py <input_image:image> <save_image?:boolean>`

-   input_image
    -   The input image that wants to be detected for faces
        -   can be any type of image that is a jpeg or png (others are not tested yet)

    -   save_image?
        -   gives the option to save the output image
            -   either be a boolean (true or false)

-   What will happen?
    -   A pop-up box will appear showing the input images with red rectangles around every face it detects

## What have i learned?
-   opencv2
    -   how to display image and stuff
-   haar cascade
    -   needing to convert to grayscale
    -   scaleFactor and what will happen if there is no scaleFactor
    -   minNeighbors