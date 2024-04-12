import turtle
import random

def pick_word(wordslist):
    '''
    A function that takes a list of words as an input and randomly selects and
    returns one of them.
    '''
    dict_length = len(wordslist)
    rand_num = random.randint(dict_length)
    game_word = wordslist[rand_num]
    return game_word

def draw_man(turt, text, error_count):
    '''
    A function that draws the different parts based on the updated error count
    '''
    turt.up()
    text.up()
    text.goto(100, 0)
    text.down()
    for cnt in range(error_count):
        text.clear()
        text.write(
        turt.up()
        turt.goto(-100, 0)
        turt.down()
        turt.setheading(270)
        if cnt == 0:
            turt.goto(-150, 0)
            turt.circle(50)
        elif cnt == 0:
            turt.setheading(270)
            turt.forward(100)
        elif cnt == 2:
            turt.setheading(315)
            turt.forward(100)
        elif cnt == 3:
            turt.up()
            turt.goto(-100, -100)
            turt.setheading(225)
            turt.down()
            turt.forward(100)
        elif cnt == 4:
            turt.up()
            turt.goto(-100, -100)
            turt.setheading(315)
            turt.down()
            turt.forward(100)


# def main():
win = turtle.Screen()
man = turtle.Turtle()
text = turtle.Turtle()

man.speed(0)
draw_man(man, text, 5)

win.exitonclick()