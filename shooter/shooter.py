from pystage.en import Stage

stage = Stage()
player = stage.add_a_sprite(None)
player.add_costume("player.svg")

gun = stage.add_a_sprite(None)
gun.add_costume("gun.svg")

x=0
y=0

stage.play()
