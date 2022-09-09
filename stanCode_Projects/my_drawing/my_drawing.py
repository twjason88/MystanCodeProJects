"""
File: 
Name: Jason Hsu
----------------------
This program draws a Minion saying hello to humans.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Greeting from Minions

    This is a Minion coming from outer space. It wants to find whether there are any species in the multi-universe
    useful that can assist them in ruling the whole universe. This time, it arrives in the Universe 234
    landing on the moon and targeting creatures on the earth. This is the way it says hi to humans.
    """
    window = GWindow(width=500, height=500, title='Jason')

    back_ground = GRect(window.width, window.height)
    back_ground.filled = True
    back_ground.fill_color = 'black'
    window.add(back_ground)

    star_back = GRect(75, 200)
    star_back.filled = True
    star_back.fill_color = 'ivory'
    window.add(star_back, -25, -50)

    star1 = GOval(50, 100)
    star1.filled = True
    window.add(star1, -25, -50)

    star2 = GOval(50, 100)
    star2.filled = True
    window.add(star2, 25, -50)

    star3 = GOval(50, 100)
    star3.filled = True
    window.add(star3, 25, 50)

    star4 = GOval(50, 100)
    star4.filled = True
    window.add(star4, -25, 50)

    face = GOval(130, 130)
    face.filled = True
    face.fill_color = 'gold'
    window.add(face, x=(window.width-face.width)/2, y=(window.height-face.height)/2 - 60)

    body = GRect(130, 150)
    body.filled = True
    body.fill_color = 'gold'
    window.add(body, x=(window.width-face.width)/2, y=(window.height-face.height)/2 - 10)

    left_hand = GPolygon()
    left_hand.add_vertex(((window.width - face.width) / 2, 252))
    left_hand.add_vertex(((window.width - face.width) / 2, 262))
    left_hand.add_vertex(((window.width - face.width) / 2 - 32, 272))
    left_hand.add_vertex(((window.width - face.width) / 2 - 35, 262))
    left_hand.filled = True
    left_hand.fill_color = 'gold'
    window.add(left_hand)

    right_hand = GPolygon()
    right_hand.add_vertex(((window.width - face.width) / 2 + 130, 252))
    right_hand.add_vertex(((window.width - face.width) / 2 + 165, 242))
    right_hand.add_vertex(((window.width - face.width) / 2 + 168, 252))
    right_hand.add_vertex(((window.width - face.width) / 2 + 130, 262))
    right_hand.filled = True
    right_hand.fill_color = 'gold'
    window.add(right_hand)

    right_finger = GOval(15, 15)
    right_finger.filled = True
    right_finger.color = 'snow'
    window.add(right_finger, 345, 239)

    eye_glass = GOval(70, 70)
    eye_glass.filled = True
    window.add(eye_glass, x=(window.width-face.width)/2 + 30, y=(window.height-face.height)/2 - 40)

    eye = GOval(55, 55)
    eye.filled = True
    eye.fill_color = 'white'
    window.add(eye, x=(window.width-face.width)/2 + 37, y=(window.height-face.height)/2 - 33)

    eyeball = GOval(30, 30)
    eyeball.filled = True
    window.add(eyeball, x=(window.width - face.width) / 2 + 50, y=(window.height - face.height) / 2 - 20)

    eye_belt_left = GRect(40, 15)
    eye_belt_left.filled = True
    window.add(eye_belt_left, x=(window.width-face.width)/2 - 7, y=(window.height-face.height)/2 - 15)

    eye_belt_right = GRect(40, 15)
    eye_belt_right.filled = True
    window.add(eye_belt_right, x=(window.width - face.width) / 2 + 97, y=(window.height - face.height) / 2 - 15)

    mouth = GOval(15, 15)
    mouth.filled = True
    window.add(mouth, x=(window.width - face.width) / 2 + 57, y=(window.height - face.height) / 2 + 40)

    moon = GOval(600, 250)
    moon.filled = True
    moon.fill_color = 'gainsboro'
    window.add(moon, x=(window.width-face.width)/2 - 240, y=(window.height-face.height)/2 + 150)

    left_leg = GRect(25, 35)
    left_leg.filled = True
    left_leg.fill_color = 'cornflowerblue'
    left_leg.color = 'cornflowerblue'
    window.add(left_leg, x=(window.width - face.width) / 2 + 35, y=(window.height - face.height) / 2 + 150)

    hole3 = GOval(90, 60)
    hole3.filled = True
    hole3.fill_color = 'lightgray'
    hole3.color = 'lightgray'
    window.add(hole3, x=340, y=370)

    shadow = GOval(150, 10)
    shadow.filled = True
    shadow.fill_color = 'black'
    window.add(shadow, x=(window.width - face.width) / 2 + 80, y=(window.height - face.height) / 2 + 180)

    right_leg = GRect(25, 35)
    right_leg.filled = True
    right_leg.fill_color = 'cornflowerblue'
    right_leg.color = 'cornflowerblue'
    window.add(right_leg, x=(window.width - face.width) / 2 + 70, y=(window.height - face.height) / 2 + 150)

    bottom = GOval(130, 60)
    bottom.filled = True
    bottom.fill_color = 'cornflowerblue'
    bottom.color = 'cornflowerblue'
    window.add(bottom, x=(window.width - face.width) / 2, y=(window.height - face.height) / 2 + 110)

    cloth = GPolygon()
    cloth.add_vertex(((window.width-face.width)/2, 240))
    cloth.add_vertex(((window.width-face.width)/2 + 30, 250))
    cloth.add_vertex(((window.width - face.width) / 2 + 105, 250))
    cloth.add_vertex(((window.width - face.width) / 2 + 130, 240))
    cloth.add_vertex(((window.width - face.width) / 2 + 135, 250))
    cloth.add_vertex(((window.width - face.width) / 2 + 105, 260))
    cloth.add_vertex(((window.width - face.width) / 2 + 105, 295))
    cloth.add_vertex(((window.width - face.width) / 2 + 130, 295))
    cloth.add_vertex(((window.width - face.width) / 2 + 130, 325))
    cloth.add_vertex(((window.width - face.width) / 2, 325))
    cloth.add_vertex(((window.width - face.width) / 2, 295))
    cloth.add_vertex(((window.width - face.width) / 2 + 30, 295))
    cloth.add_vertex(((window.width - face.width) / 2 + 30, 260))
    cloth.add_vertex(((window.width - face.width) / 2 - 5, 250))
    cloth.filled = True
    cloth.fill_color = 'cornflowerblue'
    cloth.color = 'cornflowerblue'
    window.add(cloth)

    pocket = GPolygon()
    pocket.add_vertex(((window.width-face.width)/2 + 45, 270))
    pocket.add_vertex(((window.width - face.width) / 2 + 90, 270))
    pocket.add_vertex(((window.width - face.width) / 2 + 90, 305))
    pocket.add_vertex(((window.width - face.width) / 2 + 45, 305))
    pocket.filled = True
    pocket.fill_color = 'royalblue'
    pocket.color = 'royalblue'
    window.add(pocket)

    left_shoe = GRect(30, 5)
    left_shoe.filled = True
    window.add(left_shoe, x=(window.width - face.width) / 2 + 30, y=(window.height - face.height) / 2 + 185)

    right_shoe = GRect(30, 5)
    right_shoe.filled = True
    window.add(right_shoe, x=(window.width - face.width) / 2 + 70, y=(window.height - face.height) / 2 + 185)

    flag = GRect(150, 100)
    flag.filled = True
    flag.fill_color = 'mediumturquoise'
    window.add(flag, x=(window.width-face.width)/2 - 180, y=(window.height-face.height)/2 - 73)

    bar_left = GRect(5, 200)
    bar_left.filled = True
    bar_left.fill_color = 'burlywood'
    bar_left.color = 'burlywood'
    window.add(bar_left, x=(window.width-face.width)/2 - 35, y=(window.height-face.height)/2 - 73)

    left_finger = GOval(15, 15)
    left_finger.filled = True
    left_finger.color = 'snow'
    window.add(left_finger, x=(window.width-face.width)/2 - 40, y=259)

    hole = GOval(90, 60)
    hole.filled = True
    hole.fill_color = 'lightgray'
    hole.color = 'lightgray'
    window.add(hole, x=100, y=350)

    hole2 = GOval(90, 60)
    hole2.filled = True
    hole2.fill_color = 'lightgray'
    hole2.color = 'lightgray'
    window.add(hole2, x=200, y=400)

    hole4 = GOval(90, 60)
    hole4.filled = True
    hole4.fill_color = 'lightgray'
    hole4.color = 'lightgray'
    window.add(hole4, x=30, y=410)

    hole5 = GOval(90, 60)
    hole5.filled = True
    hole5.fill_color = 'lightgray'
    hole5.color = 'lightgray'
    window.add(hole5, x=370, y=450)

    label1 = GLabel('Hello,\nhumans!')
    label1.font = 'Times New Roman-35-bold'
    label1.color = 'tomato'
    window.add(label1, 15, 205)

    label2 = GLabel('Jason')
    label2.font = 'Times New Roman-15-italic'
    label2.color = 'blue'
    window.add(label2, 235, 295)


if __name__ == '__main__':
    main()
