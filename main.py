import cv2
from sys import argv

# Set thei input image to be a image given as an argument when running the program
input_image = cv2.imread(argv[1])

# load the classifier or the cascade (dataset)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img is img source
# classifier is the haar cascade (aka xml file)
# scaleFactor is when the image is scaled down for the machine to detect faces
# minNeighbors is how many 'tests' is it to approve that the face is actually a face

def draw_box(img, classifier, scaleFactor, minNeighbors, color):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # it can detect faces in grayscale
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

    # for the coords in the features
    for (x,y,w,h) in features:

        # draw a rectangle
        # x,y is the top left corner
        # x + w is the top right corner
        # x + h is the bottom left corner
        # (x+w) + (y+h) is the bottom right corner

        # cv2.rectangle needs 5 args
        # first is img source (the one is RGB or BGR)
        # second is the top left point
        # third is the bottom right point
        # fourth is the color
        # fifth is the border size (-1 to fill)
        cv2.rectangle(img, (x,y) , (x + w, y + h), color, 2)

    return img

# runs in a loop
while True:

    # img is the input_image we gave
    img = input_image
    
    # draw_box is the function we defined on top
    # color is in a tuple: (b,g,r)
    draw_box(img, face_classifier, 1.3, 10, (0,0,255))

    # show the image (first is the window name, second is the source)
    cv2.imshow('nice', img)

    # conventional way to quit the program by pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()