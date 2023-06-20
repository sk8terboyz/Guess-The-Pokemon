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


# answers
answers = data['answers']

class Menu:
    def __init__(self):
                
        # display menu
        self.display_menu()
        

        # display menu to choose generation
    def display_menu(self):
        
        global menu_label, gen1_btn, gen2_btn, gen3_btn, gen4_btn, gen5_btn
        
        menu_label = Label(root, text="Choose which gen to play", font=("Algerian", 24, "bold")).place(x=200, y=100)
        
        gen1_btn = Button(root, text="gen1", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(1)).place(x=200, y=200)
        gen2_btn = Button(root, text="gen2", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(2)).place(x=500, y=200)
        gen3_btn = Button(root, text="gen3", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(3)).place(x=200, y=300)
        gen4_btn = Button(root, text="gen4", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(4)).place(x=500, y=300)
        gen5_btn = Button(root, text="gen5", font=("Algerian", 16, "bold"), padx=20, pady=20, command=lambda: self.remove_menu(5)).place(x=350, y=400)
    
    def remove_menu(self, gen):
        game = Guess_The_Pokemon()
        
        root.destroy()
        game.start_game(gen)
    
class Guess_The_Pokemon:
    
    def __init__(self):
        # set question number
        self.question_num = 0
        
        # selected choice
        self.choice = IntVar()
        
        # current image chosen
        self.current_image = IntVar()
        
        # list of images already used to avoid duplications during game
        self.previous_images = []
    

    def start_game(self, gen):
        # set gen choice from menu
        self.gen = gen
        
        # root of game GUI
        game_root = Tk()
        
        # title of window
        game_root.title("Pokemon Quiz")

        # size of window
        game_root.geometry('800x680')
        
        # store root of game window
        self.root = game_root
        
        # display title
        self.display_title()
        
        # set images based on gen choice
        self.set_gen_images()
        
        # display blacked image
        self.display_new_image()
        
        # display choices
        self.display_choices()
    
    # set images based on gen choice
    def set_gen_images(self):
        # store blacked out images
        self.blacked_images = data['blacked_images'][f'gen{self.gen}']
        # store colored images
        self.filled_images = data['images'][f'gen{self.gen}']
    
    # display title
    def display_title(self):
        Label(self.root, text="Who's That Pokemon", bg="green", fg="white", width=38, font=("Algerian", 24, "bold")).place(x=0, y=2)
        
    # check answer
    def check_answer(self):
        # method used in previous project, may use a different method
        if self.choice.get() == answers[self.question_num]:
            return True
    
    # display correct image - I want to animate this (not sure how to with tkinter yet though)
    def display_colored_image(self):
        return
    
    # display next blacked out image
    def display_new_image(self):
        # choose random image
        self.current_image = random.randint(0, len(self.blacked_images)-1)
        
        # store & display current blacked out image
        base_img = Image.open(self.blacked_images[self.current_image])
        base_img = base_img.resize((300, 250))
        img = ImageTk.PhotoImage(base_img)
        holder = Label(self.root, image=img)
        # not sure why the "image=img" doesn't work but image has to be set again to display on window
        holder.image = img
        holder.place(x=250, y=100)
        
        print(f"new image from gen {self.gen} - index={self.current_image}")
    
    # display choices
    def display_choices(self):
        Button(self.root, command=self.display_new_image, width=10, bg='blue', fg='white', text="new image", font=('algerian', 16, 'bold')).place(x=300, y=400)
        return

menu = Menu()

root.mainloop()


# Goals: 
#       Display blacked out image of a random pokemon from a specific gen - eventually add way to use multiple gens
#       Display 4 options to choose from - I'm thinking image text buttons
#       Display check button and tell user if they got it right or not
#       Display colored image of pokemon after guess is made - I want to animate this but I'm not entirely sure how with tkinter yet
