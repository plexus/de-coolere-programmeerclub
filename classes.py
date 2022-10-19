import time

class Bal:
  def __init__(self,x,y,size,velocity):
    self.x = x
    self.y = y
    self.size = size
    self.velocity = velocity

  def move(self):
    self.x += self.velocity[0]
    self.y += self.velocity[1]

  def __str__(self):
    return f"Bal(x={self.x},y={self.y})"

bal = Bal(50, 70, 10, (5,2))

while True:
  print(bal)
  bal.move()
  time.sleep(1)
