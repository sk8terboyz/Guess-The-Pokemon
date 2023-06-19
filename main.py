from tkinter import *
from PIL import ImageTk, Image
import random
import json

# root of GUI
root = Tk()

# title of window
root.title("Pokemon Quiz")

# size of window
root.geometry('800x680')

with open('data.json') as f:
    data = json.load(f)

# blacked out images
blacked_gen1 = data['blacked_images']['gen1']
# colored images
gen1 = data['images']['gen1']
# answers
answers = data['answers']

class Menu:
    def __init__(self):
                
        # display menu
        self.display_menu()
        

        # display menu to choose generation
    def display_menu(self):
        
        global menu_label, gen1_btn, gen2_btn, gen3_btn, gen4_btn, gen5_btn
        
        menu_label = Label(text="Choose which gen to play", font=("Algerian", 24, "bold")).place(x=200, y=100)
        
        gen1_btn = Button(text="gen1", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(1)).place(x=200, y=200)
        gen2_btn = Button(text="gen2", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(2)).place(x=500, y=200)
        gen3_btn = Button(text="gen3", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(3)).place(x=200, y=300)
        gen4_btn = Button(text="gen4", font=("Algerian", 16, "bold"), padx=10, pady=10, command=lambda: self.remove_menu(4)).place(x=500, y=300)
        gen5_btn = Button(text="gen5", font=("Algerian", 16, "bold"), padx=10, pady=10, command=lambda: self.remove_menu(5)).place(x=350, y=400)
    
    def remove_menu(self, gen):
        game = Guess_The_Pokemon(gen)
        
        game.start_game()
        root.destroy()
    
class Guess_The_Pokemon:
    
    def __init__(self, gen):
        
        # set question number
        self.question_num = 0
            
        # gen choice from menu
        self.gen = gen
        
        # selected choice
        self.choice = IntVar()
    

    def start_game(self):

        # root of game GUI
        game_root = Tk()
        
        # title of window
        game_root.title("Pokemon Quiz")

        # size of window
        game_root.geometry('800x680')
        
        # display title
        self.display_title(game_root)
        
        # display blacked image
        self.display_new_image()
        
        # display choices
        self.display_choices()
    
    # set images based on gen choice
    def set_gen_images(self):
        
        print()
    
    # display title
    def display_title(self, game_root):
        Label(game_root, text="Who's That Pokemon", bg="green", fg="white", width=50, font=("Algerian", 24, "bold")).place(x=0, y=2)
        
    # check answer
    def check_answer(self):
        if self.choice.get() == answers[self.question_num]:
            return True
    
    # display correct image - I want to animate this (not sure how to with tkinter yet though)
    def display_colored_image(self, game_root):
        print()
    
    # display next blacked out image
    def display_new_image(self):
        print()
    
    # display choices
    def display_choices(self):
        print()

root.mainloop()


# Goals: 
#       Display blacked out image of a random pokemon from a specific gen - eventually add way to use multiple gens
#       Display 4 options to choose from - I'm thinking image text buttons
#       Display check button and tell user if they got it right or not
