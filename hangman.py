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
    A function that draws the different parts based on the updated error count,
    and writes how many available errors are remaining
    '''
    turt.up()
    text.up()
    text.goto(100, 0)
    text.down()

    for cnt in range(error_count):
        text.clear()
        error_message = 'Errors remaining', 5 - cnt
        text.write(error_message)

        turt.up()
        turt.goto(-100, 0)
        turt.down()
        turt.setheading(270)
        if cnt == 0:
            turt.up()
            turt.goto(-150, 50)
            turt.down()
            turt.circle(50)
        elif cnt == 1:
            turt.setheading(270)
            turt.forward(100)
        elif cnt == 2:
            turt.setheading(315)
            turt.forward(100)
        elif cnt == 3:
            turt.setheading(225)
            turt.forward(100)
        elif cnt == 4:
            turt.up()
            turt.goto(-100, -100)
            turt.setheading(225)
            turt.down()
            turt.forward(100)
        elif cnt == 5:
            turt.up()
            turt.goto(-100, -100)
            turt.setheading(315)
            turt.down()
            turt.forward(100)
            text.clear()
            text.write("YOU LOSE :(")
            turt.up()
            turt.goto(-125, 50)
            turt.setheading(135)
            turt.down()
            for i in range(4):
                turt.forward(10)
                turt.back(10)
                turt.left(90)
            turt.up()
            turt.goto(-75, 50)
            turt.setheading(135)
            turt.down()
            for i in range(4):
                turt.forward(10)
                turt.back(10)
                turt.left(90)


def play_game():
    ...


# def main():
win = turtle.Screen()
man = turtle.Turtle()
text = turtle.Turtle()

man.speed(0)
draw_man(man, text, 6)

win.exitonclick()