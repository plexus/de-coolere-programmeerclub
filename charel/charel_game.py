# charel_game (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('mario')
stage.add_backdrop('maroi2')
stage.add_backdrop('mario3')
stage.add_backdrop('achtergrond2')
stage.add_backdrop('achtergrond1')
stage.add_backdrop('achtergrond3')
stage.add_backdrop('sigaret')
stage.add_backdrop('achtergrond4')
stage.add_backdrop('stippen')
stage.add_backdrop('achtergrond5')
stage.add_backdrop('achtergrond6')
stage.add_backdrop('achtergrond7')
stage.add_backdrop('boss')
stage.add_backdrop('achtergrond8')
stage.create_variable('mijn variabele')
stage.create_variable('Y vilosety')

sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(41.00000000000001)
sprite1.set_y(-25)
sprite1.go_to_back_layer()
sprite1.go_forward(15)
sprite1.point_in_direction(0)
sprite1.set_size_to(50)
sprite1.add_costume('charel', center_x=63.276016206291445, center_y=67.96116877262662)
sprite1.add_costume('angry_charel', center_x=61.77451135507869, center_y=70.05004218607621)
sprite1.next_costume()

def when_program_starts_1(self):
    self.say_for_seconds("Hallo!", 2.0)
    self.say_for_seconds("ik ben charel", 2.0)
    self.say_for_seconds("haal voor mij een mes ", 2.0)
    self.say_for_seconds("wan anders lik ik u voeten,", 2.0)

sprite1.when_program_starts(when_program_starts_1)

def when_program_starts_2(self):
    while True:
        if self.key_pressed("right arrow"):
            self.point_in_direction(90.0)
            self.move(10.0)

        if self.key_pressed("left arrow"):
            self.point_in_direction(-90.0)
            self.move(10.0)

sprite1.when_program_starts(when_program_starts_2)

def when_program_starts_3(self):
    self.set_variable("Y vilosety", 0)
    while True:
        if self.touching_color((228, 0, 0)):
            self.set_variable("Y vilosety", 0)
            self.wait(0.5)
            while not not (self.touching_color((228, 0, 0))):
                self.change_y_by(1.0)
        else:
            self.change_variable_by("Y vilosety", -2.0)

        self.change_y_by(self.get_variable("Y vilosety"))

sprite1.when_program_starts(when_program_starts_3)

def when_program_starts_4(self):
    while True:
        if self.key_pressed("up arrow"):
            self.point_in_direction(0.0)
            self.move(80.0)
            self.wait(0.3)

sprite1.when_program_starts(when_program_starts_4)

def when_program_starts_5(self):
    while True:
        if self.touching_color((0, 184, 24)):
            self.switch_backdrop_to("maroi2")
            self.glide_to_x_y(0.0, -204.0, -168.0)

sprite1.when_program_starts(when_program_starts_5)

def when_program_starts_6(self):
    self.switch_backdrop_to("mario")
    self.glide_to_x_y(0.0, 175.0, -174.0)

sprite1.when_program_starts(when_program_starts_6)

def when_program_starts_7(self):
    while True:
        if self.touching_color((255, 247, 19)):
            self.glide_to_x_y(0.0, -209.0, -164.0)

sprite1.when_program_starts(when_program_starts_7)

def when_program_starts_8(self):
    while True:
        if self.touching_color((255, 247, 0)):
            self.glide_to_x_y(0.0, 169.0, -183.0)

sprite1.when_program_starts(when_program_starts_8)

def when_program_starts_9(self):
    while True:
        if self.touching_color((222, 0, 204)):
            self.switch_backdrop_to("mario3")
            self.set_size_to(40.0)
            self.glide_to_x_y(0.0, -204.0, -168.0)

sprite1.when_program_starts(when_program_starts_9)

def when_program_starts_10(self):
    while True:
        if self.touching_color((0, 230, 255)):
            self.switch_backdrop_to("achtergrond2")
            self.set_size_to(40.0)
            self.glide_to_x_y(0.0, 212.0, -167.0)

sprite1.when_program_starts(when_program_starts_10)

def when_program_starts_11(self):
    while True:
        if self.touching_color((105, 105, 105)):
            self.switch_backdrop_to("achtergrond1")
            self.set_size_to(10.0)
            self.glide_to_x_y(0.0, -30.0, 123.0)

sprite1.when_program_starts(when_program_starts_11)

def when_program_starts_12(self):
    while True:
        if self.touching_color((0, 0, 0)):
            self.glide_to_x_y(0.0, 211.0, -169.0)

sprite1.when_program_starts(when_program_starts_12)

def when_program_starts_13(self):
    while True:
        if self.touching_color((175, 5, 227)):
            self.switch_backdrop_to("achtergrond3")
            self.set_size_to(10.0)
            self.glide_to_x_y(0.0, -30.0, 123.0)

sprite1.when_program_starts(when_program_starts_13)

def when_program_starts_14(self):
    while True:
        if self.touching_color((210, 34, 15)):
            self.glide_to_x_y(3.0, -30.0, 123.0)

sprite1.when_program_starts(when_program_starts_14)

def when_program_starts_15(self):
    self.set_size_to(50.0)

sprite1.when_program_starts(when_program_starts_15)

def when_program_starts_16(self):
    while True:
        if self.touching_color((191, 0, 250)):
            self.switch_backdrop_to("sigaret")
            self.set_size_to(10.0)
            self.glide_to_x_y(0.0, -199.0, -170.0)

sprite1.when_program_starts(when_program_starts_16)

def when_program_starts_17(self):
    while True:
        if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
            self.switch_costume_to("angry_charel")
            self.set_size_to(50.0)

sprite1.when_program_starts(when_program_starts_17)

def when_program_starts_18(self):
    self.switch_costume_to("charel")
    self.set_size_to(55.0)

sprite1.when_program_starts(when_program_starts_18)

def when_program_starts_19(self):
    while True:
        if self.touching_color((242, 255, 115)):
            self.switch_backdrop_to("achtergrond4")
            self.set_size_to(55.0)
            self.glide_to_x_y(0.0, -211.0, -159.0)

sprite1.when_program_starts(when_program_starts_19)

def when_program_starts_20(self):
    while True:
        if self.touching_color((0, 151, 163)):
            self.switch_backdrop_to("stippen")
            self.set_size_to(60.0)
            self.glide_to_x_y(0.0, -205.0, -169.0)

sprite1.when_program_starts(when_program_starts_20)

def when_program_starts_21(self):
    while True:
        if self.touching_color((96, 176, 0)):
            self.switch_backdrop_to("achtergrond5")
            self.set_size_to(20.0)
            self.glide_to_x_y(0.0, 4.0, 159.0)

sprite1.when_program_starts(when_program_starts_21)

def when_program_starts_22(self):
    while True:
        if self.touching_color((173, 48, 48)):
            self.glide_to_x_y(0.0, 4.0, 159.0)

sprite1.when_program_starts(when_program_starts_22)

def when_program_starts_23(self):
    while True:
        if self.touching_color((0, 187, 124)):
            self.switch_backdrop_to("achtergrond6")
            self.set_size_to(40.0)
            self.glide_to_x_y(0.0, -228.0, -25.0)

sprite1.when_program_starts(when_program_starts_23)

def when_program_starts_24(self):
    while True:
        if self.touching_color((183, 134, 255)):
            self.glide_to_x_y(0.0, -217.0, -110.0)

sprite1.when_program_starts(when_program_starts_24)

def when_program_starts_25(self):
    while True:
        if self.touching_color((44, 225, 67)):
            self.switch_backdrop_to("achtergrond7")
            self.set_size_to(25.0)
            self.glide_to_x_y(0.0, -3.0, -174.0)

sprite1.when_program_starts(when_program_starts_25)

def when_program_starts_26(self):
    while True:
        if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
            self.glide_to_x_y(0.0, -3.0, -174.0)

sprite1.when_program_starts(when_program_starts_26)

def when_program_starts_27(self):
    while True:
        if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
            self.glide_to_x_y(0.0, -3.0, -174.0)

   sprite1.when_program_starts(when_program_starts_27)

def when_program_starts_28(self):
    while True:
        if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
            self.glide_to_x_y(0.0, -3.0, -174.0)

sprite1.when_program_starts(when_program_starts_28)
self.when_backdrop_switches_to("boss")
self.set_size_to(50.0)
def when_program_starts_29(self):
    while True:
        if self.touching_color((0, 136, 63)):
            self.switch_backdrop_to("boss")
            self.set_size_to(25.0)
            self.glide_to_x_y(0.0, -201.0, -164.0)

sprite1.when_program_starts(when_program_starts_29)

def when_program_starts_30(self):
    while True:
        if {{CONDITION}}:
            {{SUBSTACK | indent(4)}}


sprite1.when_program_starts(when_program_starts_30)

def when_program_starts_31(self):
    self.hide_variable("Y vilosety")

sprite1.when_program_starts(when_program_starts_31)

sprite4 = stage.add_a_sprite(None)
sprite4.set_name("Sprite4")
sprite4.set_x(148.5714048947831)
sprite4.set_y(-69.55190148374882)
sprite4.go_to_back_layer()
sprite4.go_forward(11)
sprite4.point_in_direction(28.686883977904813)
sprite4.hide()
sprite4.add_costume('uiterlijk1', center_x=10, center_y=10.6875)
sprite4.add_sound('plop')

def when_program_starts_32(self):
    self.hide()

sprite4.when_program_starts(when_program_starts_32)
self.when_backdrop_switches_to("achtergrond2")
self.show()
while True:
    self.move(10.0)
    self.if_on_edge_bounce()
    self.set_size_to(100.0)
self.when_backdrop_switches_to("achtergrond1")
self.hide()
sprite5 = stage.add_a_sprite(None)
sprite5.set_name("Sprite5")
sprite5.set_x(95.8482141494759)
sprite5.set_y(78.62005018125095)
sprite5.go_to_back_layer()
sprite5.go_forward(10)
sprite5.point_in_direction(-168.4630409671845)
sprite5.hide()
sprite5.add_costume('uiterlijk1_2', center_x=11, center_y=9.6875)
sprite5.add_sound('plop')
self.when_backdrop_switches_to("achtergrond1")
self.hide()
self.when_backdrop_switches_to("achtergrond2")
self.show()
while True:
    self.move(10.0)
    self.if_on_edge_bounce()
    self.set_size_to(100.0)
def when_program_starts_33(self):
    self.hide()

sprite5.when_program_starts(when_program_starts_33)

sprite2 = stage.add_a_sprite(None)
sprite2.set_name("Sprite2")
sprite2.set_x(-92.83797479880576)
sprite2.set_y(7.462211572384026)
sprite2.go_to_back_layer()
sprite2.go_forward(9)
sprite2.point_in_direction(158.68610254344145)
sprite2.hide()
sprite2.add_costume('uiterlijk1_2', center_x=11, center_y=9.6875)
sprite2.add_sound('plop')
self.when_backdrop_switches_to("achtergrond1")
self.hide()
def when_program_starts_34(self):
    self.hide()

sprite2.when_program_starts(when_program_starts_34)
self.when_backdrop_switches_to("achtergrond2")
self.show()
while True:
    self.move(10.0)
    self.if_on_edge_bounce()
    self.set_size_to(100.0)
sprite7 = stage.add_a_sprite(None)
sprite7.set_name("Sprite7")
sprite7.set_x(14)
sprite7.set_y(-128)
sprite7.go_to_back_layer()
sprite7.go_forward(1)
sprite7.hide()
sprite7.add_costume('sigaret_2', center_x=2.486778669451212, center_y=28.592742585826244)
sprite7.add_sound('plop')

def when_program_starts_35(self):
    self.hide()

sprite7.when_program_starts(when_program_starts_35)
self.when_backdrop_switches_to("sigaret")
self.show()
self.glide_to_x_y(0.0, 14.0, -128.0)
self.set_size_to(100.0)
self.when_backdrop_switches_to("sigaret")
self.say_for_seconds("Hallo!", 2.0)
self.say_for_seconds("ik ben mes", 2.0)
self.say_for_seconds("steek iemand neer met mij", 2.0)
self.say_for_seconds("veel plezier", 2.0)
self.when_backdrop_switches_to("sigaret")
while True:
    if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        self.hide()
sprite3 = stage.add_a_sprite(None)
sprite3.set_name("Sprite3")
sprite3.set_x(-275)
sprite3.set_y(7.000000000005551)
sprite3.go_to_back_layer()
sprite3.go_forward(2)
sprite3.point_in_direction(-90)
sprite3.hide()
sprite3.add_costume('platform_1', center_x=46.75, center_y=14.4375)
sprite3.add_sound('plop')

def when_program_starts_36(self):
    self.hide()

sprite3.when_program_starts(when_program_starts_36)
self.when_backdrop_switches_to("achtergrond4")
self.show()
self.glide_to_x_y(0.0, 133.0, 7.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    self.move(10.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((41, 15, 173)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((29, 0, 173)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("stippen")
self.hide()
sprite6 = stage.add_a_sprite(None)
sprite6.set_name("Sprite6")
sprite6.set_x(275)
sprite6.set_y(-136)
sprite6.go_to_back_layer()
sprite6.go_forward(4)
sprite6.hide()
sprite6.add_costume('platform_1', center_x=46.75, center_y=14.4375)
sprite6.add_sound('plop')

def when_program_starts_37(self):
    self.hide()

sprite6.when_program_starts(when_program_starts_37)
self.when_backdrop_switches_to("achtergrond4")
self.show()
self.glide_to_x_y(0.0, -151.0, -136.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    self.move(10.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((41, 15, 173)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((29, 0, 173)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("stippen")
self.hide()
sprite9 = stage.add_a_sprite(None)
sprite9.set_name("Sprite9")
sprite9.set_x(275)
sprite9.set_y(-59)
sprite9.go_to_back_layer()
sprite9.go_forward(5)
sprite9.hide()
sprite9.add_costume('platform_1', center_x=46.75, center_y=14.4375)
sprite9.add_sound('plop')

def when_program_starts_38(self):
    self.hide()

sprite9.when_program_starts(when_program_starts_38)
self.when_backdrop_switches_to("achtergrond4")
self.show()
self.glide_to_x_y(0.0, -3.0, -59.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    self.move(10.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((41, 15, 173)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((29, 0, 173)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("stippen")
self.hide()
sprite10 = stage.add_a_sprite(None)
sprite10.set_name("Sprite10")
sprite10.set_x(264)
sprite10.set_y(-28.99999999999963)
sprite10.go_to_back_layer()
sprite10.go_forward(6)
sprite10.hide()
sprite10.add_costume('uiterlijk1_3', center_x=39.70285360385978, center_y=45.1875)
sprite10.add_sound('plop')

def when_program_starts_39(self):
    self.hide()

sprite10.when_program_starts(when_program_starts_39)
self.when_backdrop_switches_to("achtergrond7")
self.show()
self.glide_to_x_y(0.0, -158.0, -29.0)
while True:
    self.move(15.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((132, 88, 220)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((153, 102, 255)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("boss")
self.hide()
sprite11 = stage.add_a_sprite(None)
sprite11.set_name("Sprite11")
sprite11.set_x(264)
sprite11.set_y(72)
sprite11.go_to_back_layer()
sprite11.go_forward(7)
sprite11.hide()
sprite11.add_costume('uiterlijk1_3', center_x=39.70285360385978, center_y=45.1875)
sprite11.add_sound('plop')

def when_program_starts_40(self):
    self.hide()

sprite11.when_program_starts(when_program_starts_40)
self.when_backdrop_switches_to("achtergrond7")
self.show()
self.glide_to_x_y(0.0, -28.0, 72.0)
while True:
    self.move(15.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((132, 88, 220)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((153, 102, 255)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("boss")
self.hide()
sprite12 = stage.add_a_sprite(None)
sprite12.set_name("Sprite12")
sprite12.set_x(-264)
sprite12.set_y(-123)
sprite12.go_to_back_layer()
sprite12.go_forward(8)
sprite12.point_in_direction(-90)
sprite12.hide()
sprite12.add_costume('uiterlijk1_3', center_x=39.70285360385978, center_y=45.1875)
sprite12.add_sound('plop')

def when_program_starts_41(self):
    self.hide()

sprite12.when_program_starts(when_program_starts_41)
self.when_backdrop_switches_to("achtergrond7")
self.show()
self.glide_to_x_y(0.0, -9.0, -123.0)
while True:
    self.move(15.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((132, 88, 220)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("achtergrond7")
while True:
    if self.touching_color((153, 102, 255)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("boss")
self.hide()
sprite13 = stage.add_a_sprite(None)
sprite13.set_name("Sprite13")
sprite13.set_x(165)
sprite13.set_y(-93)
sprite13.go_to_back_layer()
sprite13.go_forward(14)
sprite13.set_size_to(400)
sprite13.add_costume('uiterlijk1', center_x=43, center_y=69, factor=2)
self.when_backdrop_switches_to("boss")
self.show()
self.set_size_to(400.0)
self.go_to_x_y(168.0, -121.0)
self.say_for_seconds("dag charel ik heb lang op je gewacht", 0)
self.say_for_seconds("waren mijn levels te moeilijk", 3.0)
self.say_for_seconds("ik zie dat je haai bent", 2.0)
self.say_for_seconds("maar ik blijf haaier", 2.0)
self.say_for_seconds("moehahahahahaha", 2.0)
self.wait(2.0)
self.glide_to_x_y(2.0, 46.0, 41.0)
self.wait(3.0)
self.glide_to_sprite(1.0, "NO TRANSLATION: motion_glideto_menu")
def when_program_starts_42(self):
    self.hide()

sprite13.when_program_starts(when_program_starts_42)
self.when_backdrop_switches_to("boss")
sprite14 = stage.add_a_sprite(None)
sprite14.set_name("Sprite14")
sprite14.set_x(10)
sprite14.set_y(110)
sprite14.go_to_back_layer()
sprite14.go_forward(12)
sprite14.add_costume('uiterlijk1_4', center_x=144.5, center_y=69.5)
sprite14.add_costume('uiterlijk2', center_x=144.5, center_y=69.5)
sprite14.add_costume('uiterlijk3', center_x=144.5, center_y=69.5)
sprite14.add_costume('uiterlijk4', center_x=144.5, center_y=69.5)
sprite14.add_costume('uiterlijk5', center_x=289, center_y=139, factor=2)
sprite14.add_sound('plop')
self.when_backdrop_switches_to("boss")
self.show()
self.go_to_x_y(10.0, 110.0)
self.when_backdrop_switches_to("mario")
self.hide()
def when_program_starts_43(self):
    self.hide()

sprite14.when_program_starts(when_program_starts_43)

sprite8 = stage.add_a_sprite(None)
sprite8.set_name("Sprite8")
sprite8.set_x(275)
sprite8.set_y(82)
sprite8.go_to_back_layer()
sprite8.go_forward(3)
sprite8.hide()
sprite8.add_costume('platform_1', center_x=46.75, center_y=14.4375)
sprite8.add_sound('plop')

def when_program_starts_44(self):
    self.hide()

sprite8.when_program_starts(when_program_starts_44)
self.when_backdrop_switches_to("achtergrond4")
self.show()
self.glide_to_x_y(0.0, -64.0, 82.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    self.move(10.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((41, 15, 173)):
        self.point_in_direction(-90.0)
self.when_backdrop_switches_to("achtergrond4")
while True:
    if self.touching_color((29, 0, 173)):
        self.point_in_direction(90.0)
self.when_backdrop_switches_to("stippen")
self.hide()
sprite15 = stage.add_a_sprite(None)
sprite15.set_name("Sprite15")
sprite15.set_x(10)
sprite15.set_y(100)
sprite15.go_to_back_layer()
sprite15.go_forward(13)
sprite15.set_size_to(9.206254819654067)
sprite15.add_costume('uiterlijk1_5', center_x=29.180439735310557, center_y=53.442264267498416)
sprite15.add_sound('plop')

def when_program_starts_45(self):
    self.hide()

sprite15.when_program_starts(when_program_starts_45)
self.when_backdrop_switches_to("boss")
while True:
    self.show()
    self.glide_to_x_y(0.0, 10.0, 100.0)
    self.set_size_to(0.1)
    if self.touching("NO TRANSLATION: sensing_touchingobjectmenu"):
        self.wait(3.0)
        self.go_to_sprite("NO TRANSLATION: motion_goto_menu")
stage.play()
