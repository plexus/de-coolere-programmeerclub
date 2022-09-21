from processing_py import *
app = App(600,600) # create window: width, height


import math
app.colorMode('HSB',255,255,255)
# app.background(255)
app.noStroke()
app.fill((app.millis()*0.1)%255,255,255)
w = math.sin(app.millis()*0.0015)*100
app.translate(app.mouseX, app.mouseY)
app.rotate(app.millis()*0.001)
app.rect(0,0, w, w)
app.redraw()

