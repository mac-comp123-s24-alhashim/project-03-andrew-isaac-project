import turtle
import random
import tkinter as tk

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

    for num_errors in range(error_count):
        text.clear()
        error_message = 'Errors remaining', 5 - num_errors
        text.write(error_message)

        turt.up()
        turt.goto(-100, 0)
        turt.down()
        turt.setheading(270)
        if num_errors == 0:
            turt.up()
            turt.goto(-150, 50)
            turt.down()
            turt.circle(50)

        elif num_errors == 1:
            turt.setheading(270)
            turt.forward(100)
        elif num_errors == 2:
            turt.setheading(315)
            turt.forward(100)
        elif num_errors == 3:
            turt.setheading(225)
            turt.forward(100)
        elif num_errors == 4:
            turt.up()
            turt.goto(-100, -100)
            turt.setheading(225)
            turt.down()
            turt.forward(100)
        elif num_errors == 5:
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
            turt.up()
            turt.goto(-75, 20)
            turt.setheading(90)
            turt.down()
            turt.circle(25, 180)

class BasicGui:

    def __init__(self):
        self.rootWin = tk.Tk()
        self.label_one = tk.Label(self.rootWin)
        self.label_one.grid(row=1, column=2)
        self.label_one["text"] = "Type your guess and then press enter!"
        self.entry = tk.Entry(self.rootWin)
        self.entry.grid(row=2, column=2)
        self.entry.bind("<Key-Return>", self.entry_response)

    def entry_response(self, event):
        self.guess = self.entry.get()
        print(self.guess)
        self.guess = self.guess.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        guessed_letters = []
        if self.guess not in alphabet:
            self.label_one["text"] = "Please enter a letter!"
        elif len(self.guess) != 1:
            self.label_one["text"] = "please enter only one character!"
        elif self.guess in guessed_letters:
            self.label_one["text"] = "please guess a new letter!"
        else:
            self.label_one["text"] = "Type your guess and then press enter!"
            guessed_letters.append(self.guess)
            phrase = pick_word(words)
            if self.guess in phrase:
                




    def run(self):
        self.rootWin.mainloop()


def check_guess(letter, phrase, scribe):
    scribe.up()
    scribe.goto(100, 0)
    for char in phrase:
        scribe.down()
        scribe.forward(20)
        scribe.up()
        scribe.forward(10)
    if letter in phrase:
        return True
    else:
        return False




if __name__ == '__main__':
    win = turtle.Screen()
    man = turtle.Turtle()
    text = turtle.Turtle()
    guesses = turtle.Turtle()
    man.speed(0)
    check_guess('a', 'apple', guesses)
    myGui = BasicGui()
    myGui.run()


    win.exitonclick()