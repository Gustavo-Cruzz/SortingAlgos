from manim import *
from numpy import array

class MergeVector(Scene):
    "An animation of Merge Sort on worst case scenario"
    
    def construct(self):      
        self.length = 0
        self.iter = 0
        self.squares = [[],[],[],[],[],[], [], []]
        self.texts = [[],[],[],[],[],[], [], []]  

        divide_up = array((0.0, 1.5, 0.0))

        def init_array():
            """Initializes 8 blue squares numbered in reverse order.
               Also populates separate arrays for numbers and squares
            """          
            squares = []
            texts = []

            offset = .5
            for i in range(0,8):
                square = Square()
                ft = Text(f"{7-i}", font="Comic Sans")
                square.set_fill(BLUE, opacity=0.5,).scale(.5)

                self.play(Create(VGroup(square, ft)), runtime = .5)

                self.play(square.animate.to_edge(DL).shift(RIGHT*i).shift(RIGHT), 
                        ft.animate.to_edge(DL + offset).shift(RIGHT*i + offset+.04).shift(RIGHT), 
                        run_time = .5)

                squares.append(square)
                texts.append(ft)
            
            self.iter = 1
            self.squares[self.iter] = squares
            self.texts[self.iter] = texts


        def join_arr_group(group, new_scale, movement, displace, anim_time=.2, mv_text=True):
            """Moves the cloned arrays up a single unit and
               makes sure they are close to their respective group.

            Args:
                group (list): Contains all elements in the animated array
                new_scale (int): The new scale for the cloned array
                movement (np.ndarray): Coordinates for individual element's movement
                displace (float): How much to add to movement in order to make itens 
                                  closely bounded
                anim_time (float, optional): How fast should the animations be. Defaults to .2.
            """            
            last = None

            for (i, j) in group:
                self.play(Create(i), run_time=anim_time)
                self.play(i.animate.shift(divide_up).scale(new_scale),  
                          j.animate.shift(divide_up).scale(new_scale),
                          run_time=anim_time)
                
                if last and mv_text:
                    self.play(i.animate.next_to(last, movement + displace),  
                              j.animate.next_to(last, movement),
                              run_time=anim_time)
                elif last and not(mv_text):
                    self.play(i.animate.next_to(last, movement + displace), 
                              j.animate.next_to(last),
                              run_time=.1)
                last = i


        def reposition(n1, n2, movr, movl, move=True):
            """Animates the shuffling of two elements in array

            Args:
                n1 (int): The left-most index to shuffle to the right
                n2 (int): The right-most index to shuffle to the right
                movr (float): How much movement to the left
                movl (float): How much movement to the left
                move (bool): Whether to move elements or not
            """            
            self.play(self.squares[self.iter][n1].animate.set_fill(YELLOW),
                      self.squares[self.iter][n2].animate.set_fill(YELLOW))

            if move:
                self.play(self.texts[self.iter][n1].animate.shift((movr * RIGHT)),
                        self.texts[self.iter][n2].animate.shift(movl * LEFT))
        
                self.texts[self.iter][n1], self.texts[self.iter][n2] = self.texts[self.iter][n2], self.texts[self.iter][n1]


            self.play(self.squares[self.iter][n1].animate.set_fill(BLUE),
                       self.squares[self.iter][n2].animate.set_fill(BLUE))

        
        def delete_text(texts_group):
            """Deletes all numbers on given row

            Args:
                texts_group (list): A list containing texts for chosen row
            """            
            for k in texts_group:
                self.play(FadeOut(k, shift=DOWN), run_time=.2)
            
        def delete_squares(square_group):
            """ Same as above, directed at squares
            
            Args:
                square_group (list): A list containing texts for chosen row
            """
            for k in square_group:
                self.play(FadeOut(k, shift=DOWN), run_time=.2)
            

        title = Text("""\t\t\t\t\t                  _____  ______ _______ ____  _   _                   \n\t\t\t\t\t                 |  __ \\|  ____|__   __/ __ \\| \\ | |   /\\             \n\t\t\t\t\t         ______  | |  | | |__     | | | |  | |  \\| |  /  \\     ______ \n\t\t\t\t\t        |______| | |  | |  __|    | | | |  | | . ` | / /\\ \\   |______|\n\t\t\t\t\t                 | |__| | |____   | | | |__| | |\\  |/ ____ \\          \n\t\t\t\t\t                 |_____/|______|  |_|  \\____/|_| \\_/_/    \\_\\         \n""").scale(.4)
        subtitle = Text("""\t\t\t\t\t       __  __ ______ _____   _____ ______    _____  ____  _____ _______ \n\t\t\t\t\t      |  \\/  |  ____|  __ \\ / ____|  ____|  / ____|/ __ \\|  __ \\__   __|\n\t\t\t\t\t      | \\  / | |__  | |__) | |  __| |__    | (___ | |  | | |__) | | |   \n\t\t\t\t\t      | |\\/| |  __| |  _  /| | |_ |  __|    \\___ \\| |  | |  _  /  | |   \n\t\t\t\t\t      | |  | | |____| | \\ \\| |__| | |____   ____) | |__| | | \\ \\  | |   \n\t\t\t\t\t      |_|  |_|______|_|  \\_\\\\_____|______| |_____/ \\____/|_|  \\_\\ |_|   \n\n""").scale(.4).shift(2*DOWN)
        self.play(Create(title),
                  Create(subtitle))
        self.wait(3)

        self.play(FadeOut(title,shift=DOWN),
                  FadeOut(subtitle,shift=DOWN))

        init_array()
        self.wait(1)

        new_scale = .8
        anim_time = .2

        displace = np.array((.66, 0, 0))
        group = [(i.copy(), j.copy()) for i,j in zip(self.squares[self.iter], self.texts[self.iter])]

        join_arr_group(group[:4], new_scale, RIGHT, -displace, anim_time)
        join_arr_group(group[:3:-1], new_scale, LEFT, displace, anim_time)
        
        self.iter += 1

        self.squares[self.iter] = [i for (i,j) in group]
        self.texts[self.iter] = [j for (i,j) in group]


        group = [(i.copy(), j.copy()) for i,j in zip(self.squares[self.iter], self.texts[self.iter])]

        join_arr_group(group[:2], new_scale, RIGHT, -displace, anim_time)
        join_arr_group(group[2:4], new_scale, LEFT/10, displace, anim_time, False)
        
        join_arr_group(group[4:6], new_scale, RIGHT, -displace, anim_time)
        join_arr_group(group[6:8], new_scale, LEFT/10, displace, anim_time, False)
  
        self.iter += 1
        self.squares[self.iter] = [i for (i,j) in group]
        self.texts[self.iter] = [j for (i,j) in group]


        # Merge Left Wing
        reposition(0, 1, 0.75, 0.7)
        reposition(2, 3, 0.88, 0.7)

        delete_text(self.texts[self.iter-1][:4])

        reposition(0, 2, 0.85, 0.7, move=False)
        self.play(self.texts[self.iter][2].animate.move_to(self.squares[self.iter-1][0]))
    
        
        reposition(0, 3, 0.9, 0.75, move=False)
        self.play(self.texts[self.iter][3].animate.move_to(self.squares[self.iter-1][1]))        
        
        self.play(self.texts[self.iter][0].animate.move_to(self.squares[self.iter-1][2]),
                  self.texts[self.iter][1].animate.move_to(self.squares[self.iter-1][3]))


        #Reorder values based on new animated positions
        delete_squares(self.squares[self.iter][:4])
        self.texts[self.iter][0], self.texts[self.iter][2] = self.texts[self.iter][2], self.texts[self.iter][0]
        self.texts[self.iter][1], self.texts[self.iter][3] = self.texts[self.iter][3], self.texts[self.iter][1]

        # Merge Right Wing
        delete_text(self.texts[self.iter-1][4:])
        
        reposition(4, 5, 0.65, 0.7)
        reposition(6, 7, 0.65, 0.7)

        reposition(4, 6, 0.75, 0.8, move=False)
        self.play(self.texts[self.iter][6].animate.move_to(self.squares[self.iter-1][4]))
        
        reposition(4, 7, 0.75, 0.8, move=False)
        self.play(self.texts[self.iter][7].animate.move_to(self.squares[self.iter-1][5]))
     
        self.play(self.texts[self.iter][4].animate.move_to(self.squares[self.iter-1][6]),
                  self.texts[self.iter][5].animate.move_to(self.squares[self.iter-1][7]))

        
        #Reorder values based on new animated positions
        delete_squares(self.squares[self.iter][4:])

        self.iter -= 1
        self.texts[self.iter] = self.texts[self.iter+1]
        self.texts[self.iter][4], self.texts[self.iter][6] = self.texts[self.iter][6], self.texts[self.iter][4] 
        self.texts[self.iter][5], self.texts[self.iter][7]  = self.texts[self.iter][7], self.texts[self.iter][5]

        delete_text(self.texts[self.iter-1])

        for (i,j) in ((4,0), (5,1), (6,2), (7,3)):
            reposition(i, 0, 0.9, 0.75, move=False)
            self.play(self.texts[self.iter][i].animate.move_to(self.squares[self.iter-1][j]))
        
        self.play(self.texts[self.iter][0].animate.move_to(self.squares[self.iter-1][4]),
                   self.texts[self.iter][1].animate.move_to(self.squares[self.iter-1][5]),
                   self.texts[self.iter][2].animate.move_to(self.squares[self.iter-1][6]),
                   self.texts[self.iter][3].animate.move_to(self.squares[self.iter-1][7]))

        delete_squares(self.squares[self.iter])
        self.wait(2)