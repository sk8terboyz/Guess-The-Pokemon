from tkinter import *
from PIL import ImageTk, Image
import random
import json
import time

# root of GUI
root = Tk()

# title of window
root.title("Pokemon Quiz")

# size of window
root.geometry('800x680')

with open('data.json') as f:
    data = json.load(f)

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
        
        # current image chosen
        self.current_image = IntVar()
        
        # list of images already used to avoid duplications during game
        self.previous_images = []
        
        # list of current options per question
        self.current_opts = []
        
        # choice user makes
        self.choice = IntVar()
    
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
        self.set_gen_data()
        
        # display blacked image
        self.display_new_image()
    
    # set images based on gen choice
    def set_gen_data(self):
        # store blacked out images
        self.blacked_images = data['blacked_images'][f'gen{self.gen}']
        # store colored images
        self.filled_images = data['images'][f'gen{self.gen}']
        # stored choices
        self.choices = data['choices'][f'gen{self.gen}']
    
    # display title
    def display_title(self):
        Label(self.root, text="Who's That Pokemon", bg="green", fg="white", width=38, font=("Algerian", 24, "bold")).place(x=0, y=0)
        
    # check answer
    def check_answer(self):
        print('------------')
        print(f'user choice={self.choice}')
        print(f'current_image={self.current_image}')
        print(f'self.choices[self.current_image]={self.choices[self.current_image]}')
        print('------------')
        # method used in previous project, may use a different method
        if self.choice == self.choices[self.current_image]:
            return True
        return False
    
    # animate & display if correct or not
    def animate_image(self, index_choice):
        # store user choice
        self.choice = index_choice
        
        # store & display current blacked out image
        base_img = Image.open(data['blacked_images']['blackout'])
        base_img = base_img.resize((50, 50))
        img = ImageTk.PhotoImage(base_img)
        
        # all labels used for animation
        h0 = Label(self.root, image=img)
        h1 = Label(self.root, image=img)
        h2 = Label(self.root, image=img)
        h3 = Label(self.root, image=img)
        h4 = Label(self.root, image=img)
        h5 = Label(self.root, image=img)
        h6 = Label(self.root, image=img)
        h7 = Label(self.root, image=img)
        h8 = Label(self.root, image=img)
        h9 = Label(self.root, image=img)
        h10 = Label(self.root, image=img)
        h11 = Label(self.root, image=img)
        h12 = Label(self.root, image=img)
        h13 = Label(self.root, image=img)
        h14 = Label(self.root, image=img)
        h15 = Label(self.root, image=img)
        h16 = Label(self.root, image=img)
        h17 = Label(self.root, image=img)
        h18 = Label(self.root, image=img)
        h19 = Label(self.root, image=img)
        h20 = Label(self.root, image=img)
        h21 = Label(self.root, image=img)
        h22 = Label(self.root, image=img)
        h23 = Label(self.root, image=img)
        h24 = Label(self.root, image=img)
        h25 = Label(self.root, image=img)
        h26 = Label(self.root, image=img)
        h27 = Label(self.root, image=img)
        h28 = Label(self.root, image=img)
        h29 = Label(self.root, image=img)
        # not sure why the "image=img" doesn't work but image has to be set again to display on window
        h0.image = img
        h1.image = img
        h2.image = img
        h3.image = img
        h4.image = img
        h5.image = img
        h6.image = img
        h7.image = img
        h8.image = img
        h9.image = img
        h10.image = img
        h11.image = img
        h12.image = img
        h13.image = img
        h14.image = img
        h15.image = img
        h16.image = img
        h17.image = img
        h18.image = img
        h19.image = img
        h20.image = img
        h21.image = img
        h22.image = img
        h23.image = img
        h24.image = img
        h25.image = img
        h26.image = img
        h27.image = img
        h28.image = img
        h29.image = img
        
        blackout_images = [h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,h25,h26,h27,h28,h29]
        
        horizontal = 0
        vertical = 0
        xpos = 250
        ypos = 100
        index = 0
        while vertical < 5:
            while horizontal < 6:
                blackout_images[index].place(x=xpos, y=ypos)
                time.sleep(0.05)
                self.root.update()
                xpos += 50
                index += 1
                horizontal += 1
            ypos += 50
            xpos = 250
            vertical += 1
            horizontal = 0
        
        time.sleep(0.25)
        # display colored image
        self.display_colored_image()
    
    # display correct image - I want to animate this (not sure how to with tkinter yet though)
    def display_colored_image(self):
        # display current colored image
        base_img = Image.open(self.filled_images[self.current_image])
        base_img = base_img.resize((300, 250))
        img = ImageTk.PhotoImage(base_img)
        holder = Label(self.root, image=img, bg=('green' if self.check_answer() else 'red'))
        holder.image = img
        holder.place(x=250, y=100)
        
        self.root.update()
        time.sleep(1)
        
        # end game condition
        if len(self.previous_images) == len(self.blacked_images):
            # display game over/results
            print("GAME OVER")
        else:
            self.display_new_image()
    
    # display next blacked out image
    def display_new_image(self):
        # choose random image
        rand = random.randint(0, len(self.blacked_images)-1)
        while rand in self.previous_images:
            rand = random.randint(0, len(self.blacked_images)-1)
        self.current_image = rand
        
        # add image choice to previous images
        self.previous_images.append(rand)
        
        # store & display current blacked out image
        base_img = Image.open(self.blacked_images[self.current_image])
        base_img = base_img.resize((300, 250))
        img = ImageTk.PhotoImage(base_img)
        holder = Label(self.root, image=img)
        # not sure why the "image=img" doesn't work but image has to be set again to display on window
        holder.image = img
        holder.place(x=250, y=100)
        
        # set option buttons
        self.display_choices()
    
    # display choices
    def display_choices(self):
        index_options = [0,1,2,3]
        # temp values for current_opts
        self.current_opts = [0,0,0,0]
        # correct answer index from buttons
        correct_index = random.randint(0,3)
        
        # add correct answer
        self.current_opts[correct_index] = self.choices[self.current_image]
        print(self.current_opts)
        # remove correct index from options
        index_options.remove(correct_index)
        # chosen random choices
        rand_choices = []
        rand_choices.append(self.current_image)

        # set 3 random choices from already set gen choices
        for index in range(3):
            # get random choice
            random_temp = random.randint(0, len(self.choices)-1)
            # stop duplicates
            while (random_temp not in index_options) and (self.choices[random_temp] != rand_choices[0]):
                random_temp = random.randint(0, len(self.choices)-1)
            # add random choice
            rand_choices.append(random_temp)
            # remove option from randomize process
            index_options.remove(random_temp)
            # add choice to options
            self.current_opts[random_temp] = self.choices[random_temp]
        
        print('~~~~~~~~~~~')
        print(self.current_opts)
        print('~~~~~~~~~~~')
        
        displayed_opts = []
        xpos = 200
        ypos = 400
        # add all buttons
        for x in range(4):
            # choose random option from current options
            index = random.randint(0, len(self.current_opts)-1)
            # add index from self.choices
            displayed_opts.append(self.current_opts[index])
            # create button
            Button(self.root, command=lambda: self.animate_image(displayed_opts[index]), width=10, bg="blue", fg='white', text=self.current_opts[index], font=('algerian', 16, 'bold')).place(x=xpos, y=ypos)
            if x == 1:
                # move down
                ypos += 100
                # move left
                xpos -= 200
            else:
                # move right
                xpos += 200
            # remove index after adding
            self.current_opts.pop(index)
            print('+++++++++')
            print(f"index={index}")
            print(displayed_opts)
            print('==========')
            print(self.current_opts)
            print('+++++++++')
menu = Menu()

root.mainloop()


# Goals: 
#       Display blacked out image of a random pokemon from a specific gen - eventually add way to use multiple gens
#       Display 4 options to choose from - I'm thinking image text buttons
#       Display check button and tell user if they got it right or not
#       Display colored image of pokemon after guess is made - I want to animate this but I'm not entirely sure how with tkinter yet
