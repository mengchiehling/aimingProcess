import numpy as np

# This is a quick solution of moving mouse with kmbox, no PID implemented.

eps = 10  # A hyperparameter you should choose by yourself

# You should have the coordinate of the center of image as constants
xCenter = None
yCenter = None


def _mouseMoveDrag(xOffset, yOffset):

    xOffset = int(np.round(xOffset, 0))
    yOffset = int(np.round(yOffset, 0))

    stdafx.KM_move(xOffset, yOffset)


def _distance(xOffset, yOffset, xTarget, yTarget):

    r2 = np.square(xOffset - xTarget, yOffset - yTarget)

    return np.sqrt(r2)



if __name__ == "__main__":

    # Assuming that the center of the screen is
    xOffset = None
    yOffset = None

    # xOffset, yOffset = Yolo5.detect(img)

    # km_box start moving the mouse cursor
    _mouseMoveDrag(xOffset, yOffset)

    # stop the process until the mouse cursor is sufficiently close to the center of the screen
    while _distance(xOffset=xOffset, yOffset=yOffset, xTarget=xCenter, yTarget=yCenter) >= eps:

            xOffset, yOffset = Yolo5.detect(img)

    # End of aiming process








