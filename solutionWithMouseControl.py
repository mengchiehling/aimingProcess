from pynput import mouse

m_mouse = mouse.Controller()

# x is the x-axis and y is the y-axis in convention

xCurrent, yCurrent = m_mouse.position

xOffset = None
yOffset = None

# xOffset, yOffset = Yolo5.detect(img)

m_mouse.move(xOffset - xCurrent, yOffset - yCurrent)

