from graph import *


# upper background part
penColor(11, 191, 83)
brushColor(11, 191, 83)
rectangle(0, 0, 500, 350)
# lower background part
penColor(112, 102, 108)
brushColor(112, 102, 108)
rectangle(0, 350, 500, 600)

# forest trees (orange rectangles)
penColor(242, 195, 24)
brushColor(242, 195, 24)
rectangle(0, 0, 35, 375)
rectangle(55, 0, 150, 590)
rectangle(350, 0, 385, 375)
rectangle(450, 0, 485, 425)

# hedgehog body
penSize(1)
penColor(255, 255, 255)
brushColor(85, 85, 85)
oval(250, 480, 430, 560)
oval(400, 510, 440, 535)
oval(390, 550, 415, 565)
oval(420, 535, 435, 545)
oval(270, 550, 295, 565)
oval(245, 535, 260, 545)

# mushrooms
penSize(1)
penColor(180, 180, 180)
brushColor(242, 174, 73)
circle(270, 500, 20)
circle(290, 495, 20)
brushColor(227, 46, 18)
circle(370, 495, 20)
brushColor(255, 255, 255)
oval(300, 500, 330, 450)


run()