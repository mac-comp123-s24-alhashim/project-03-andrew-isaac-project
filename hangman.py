import turtle
import random
import tkinter as tk

import wordlist
from wordlist import all_string

def pick_word(wordslist):
    """
    A function that takes a list of words as an input and randomly selects and
    returns one of them.
    """
    dict_length = len(wordslist)
    rand_num = random.randint(0, dict_length - 1)
    game_word = wordslist[rand_num]
    return game_word

def draw_man(turt, text, error_count):
    '''
    A function that draws the different parts based on the updated error count,
    and writes how many available errors are remaining
    '''
    turt.up()
    text.up()
    text.goto(100, 20)
    text.down()

    for num_errors in range(error_count):
        text.clear()
        error_message = 'Errors remaining', 5 - num_errors
        text.write(error_message, font=("Arial", 12,))

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
            text.write("YOU LOSE :(", font=("Arial", 12))
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
        self.rootWin = tk.Canvas(master=None,width=500,height=500)
        self.rootWin.pack()
        self.label_one = tk.Label(self.rootWin)
        self.label_one.grid(row=1, column=2)
        self.label_one["text"] = "Type your guess and then press enter!"
        self.entry = tk.Entry(self.rootWin)
        self.entry.grid(row=2, column=2)
        self.entry.bind("<Key-Return>", self.entry_response)


        # TODO: add quit button

        self.error_cnt = 0
        self.guessed_letters = []
        self.guessed_right_letters = 0

        self.phrase = pick_word(words_test)
        self.phrase = self.phrase.lower()
        print("FOR TESTING ONLY: PHRASE IS:", self.phrase)

        text.up()
        text.goto(100, 20)
        text.down()
        text.write('Errors remaining: 6', font=('Arial', 12))

        guesses.up()
        guesses.goto(100, 0)
        for num_letters in self.phrase:
            guesses.down()
            guesses.forward(10)
            guesses.up()
            guesses.forward(5)


    def quit_callback(self):
        self.rootWin.destroy()

    def entry_response(self, event):
        self.guess = self.entry.get()
        print(self.guess)
        self.guess = self.guess.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'



        if self.guess not in alphabet:
            self.label_one["text"] = "Please enter a letter!"
        elif len(self.guess) != 1:
            self.label_one["text"] = "please enter only one character!"
        elif self.guess in self.guessed_letters:
            self.label_one["text"] = "please guess a new letter!"
        else:
            self.label_one["text"] = "Type your guess and then press enter!"
            all_letters.clear()
            all_letters.up()
            all_letters.goto(100, -20)
            all_letters.down()
            self.guessed_letters.append(self.guess)
            str_guesses = ''.join(self.guessed_letters)
            guessed_letters_string = ("guessed letters: ", str_guesses)
            all_letters.write(guessed_letters_string, font=('Arial', 10))

            if self.guess in self.phrase:
                draw_right_answer(self.phrase, self.guess, guesses)
                new_word = self.phrase.replace(self.guess, "")
                remaining_chars = len(self.phrase) - len(new_word)
                self.guessed_right_letters = self.guessed_right_letters + remaining_chars
                print(self.guessed_right_letters)
                if self.guessed_right_letters == len(self.phrase):
                    text.clear()
                    text.write("Congratulations, you won!", font=('Arial', 12))
                    self.rootWin.destroy()

            else:
                self.error_cnt = self.error_cnt + 1
                print("ERROR_CNT value", self.error_cnt)
                draw_man(man, text, self.error_cnt)
                if self.error_cnt == 6:
                    self.rootWin.destroy()

    def run(self):
        self.rootWin.mainloop()


def draw_right_answer(correct_phrase, right_letter, guess_turtle):
    """
    A function that takes in a phrase and a letter and writes spaces for all unguessed letters,
    as well as writing the correct answer in the spaces it's supposed to go.
    """
    guess_turtle.speed(0)
    guess_turtle.up()
    guess_turtle.goto(100, 0)
    for char in correct_phrase:
        guess_turtle.down()
        if char == right_letter:
            guess_turtle.pensize(2)
            guess_turtle.forward(5)
            guess_turtle.write(char, font=('Arial', 12))
            guess_turtle.forward(5)
            guess_turtle.up()
            guess_turtle.forward(5)
        else:
            guess_turtle.down()
            guess_turtle.forward(10)
            guess_turtle.up()
            guess_turtle.forward(5)


if __name__ == '__main__':

    man = turtle.Turtle()
    man.hideturtle()
    text = turtle.Turtle()
    text.pensize(2)
    text.hideturtle()
    guesses = turtle.Turtle()
    guesses.pensize(2)
    guesses.hideturtle()
    all_letters = turtle.Turtle()
    all_letters.hideturtle()
    all_letters.pensize(2)

    man.speed(0)
    man.up()
    man.goto(-100, 100)
    man.down()
    man.left(90)
    man.forward(50)
    man.left(90)
    man.forward(100)
    man.left(90)
    man.forward(400)
    words = wordlist.return_list(all_string)
    print(words)
    words_test = ["Macalester", "Cxollege", "Squirrels", "Pants", "Bell", "Scots", "Olri", "CompSci", "Minnesota", "Science", "Python",
             "Java", "Andrew", "Isaac"]
    man.speed(0)
    myGui = BasicGui()
    myGui.run()

