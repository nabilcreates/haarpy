# Documentation
## video-test branch
-   ### lets the facial recognition run on a video file

## Usage: `python3 main.py <input_video:video>`

Video lags!
-   If you are a developer:
    -   Change the scaleFactor and the minNeighbors on line 50 on the draw_box function (which is the 3rd and 4th argument)
        -   decreasing the minNeighbors will decrease lag
        -   increasing the scaleFactor will decrease lag
            -   ### NOTE THAT THIS TAKES A TOLL ON THE ACCURACY OF THE FACE DETECTION

-   If you are just a normal person:
    -   The computer is trying to detect faces in realtime, so please be patient (a.k.a suck it up)