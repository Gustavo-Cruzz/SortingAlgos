from manim import *
from numpy import array

class CreateVector(Scene):

    def construct(self):      
        self.length = 0
        self.iter = 0
        self.squares = [[],[],[],[],[],[], [], []]
        self.texts = [[],[],[],[],[],[], [], []]  

        divide_up = array((0.0, 1.5, 0.0))
        divide_upl = array((-.5, 1.0, 0.0))
        divide_upr = array((.5, 1.0, 0.0))

        def init_array():
            """#TODO

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
            
            self.length = len(squares)
            self.iter = 1
            self.squares[self.iter] = squares
            self.texts[self.iter] = texts


        def join_arr_group(group, new_scale, movement, displace, anim_time=.2, mv_text=True):
            """Moves the cloned arrays up a single unit and
               makes sure they are close to their respective group.

            Args:
                group (list[tuple]): Contains all elements in the animated array
                new_scale (int): The new scale for the cloned array
                movement (np.ndarray): Coordinates for individual element's movement
                displace (float): How much to add to movement in order to make itens 
                                  closely bounded
                anim_time (float, optional): How fast should the animations be. Defaults to .2.
            """            
            last = None

            for (i, j) in group:
                # print(i, j)
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


        def clone_up(new_scale, anim_time=.2):
            """Makes a copy of each square and text.
               After which calls 'join_arr_group' and
               redefines the most recent elements in array

            Args:
                new_scale (int): The new scale for the cloned array
                anim_time (float, optional): How fast should the animations be. Defaults to .2.
            """            

            group = [(i.copy(), j.copy()) for i,j in zip(self.squares, self.texts)]

            group_size = int((len(group)/2))
            displace = np.array((.66, 0, 0))

            join_arr_group(group[:group_size], new_scale, RIGHT, -displace, anim_time)
            join_arr_group(group[:group_size-1:-1], new_scale, LEFT, displace, anim_time)
            
            self.length /= 2
            if self.length < 1: self.length = 1
            self.iter += 1
            self.squares[self.iter] = [i for (i,j) in group]
            self.texts[self.iter] = [j for (i,j) in group]


        def reposition(n1, n2, movr, movl, move=True, translocate=False):
            """Animates the shuffling of two elements in array

            Args:
                n1 (int): The left-most index to shuffle to the right
                n2 (int): The right-most index to shuffle to the right
            """            
            self.play(self.squares[self.iter][n1].animate.set_fill(YELLOW),
                      self.squares[self.iter][n2].animate.set_fill(YELLOW))

            if move:
                self.play(self.texts[self.iter][n1].animate.shift((movr * RIGHT)),
                        self.texts[self.iter][n2].animate.shift(movl * LEFT))
        
                self.texts[self.iter][n1], self.texts[self.iter][n2] = self.texts[self.iter][n2], self.texts[self.iter][n1]


            self.play(self.squares[self.iter][n1].animate.set_fill(BLUE),
                       self.squares[self.iter][n2].animate.set_fill(BLUE))

        
        def low_array():
            last = self.squares[self.iter-1]
            for (i,j, k,l) in zip(self.squares[self.iter], self.texts[self.iter], self.squares[self.iter-1], self.texts[self.iter-1]):
                
                self.play(i.animate.move_to(k).scale(1.2), 
                          j.animate.move_to(l).scale(1.2),
                          FadeOut(k, shift=DOWN),
                          FadeOut(l, shift=DOWN),
                          run_time=.5)

            self.iter -= 1
            self.squares[self.iter] = self.squares[self.iter +1]
            self.texts[self.iter] = self.texts[self.iter +1]

        def delete_low_text():
            for k in self.texts[self.iter-1]:
                self.play(FadeOut(k, shift=DOWN), run_time=.2)
            
        def delete_squares(group):
            for k in group:
                self.play(FadeOut(k, shift=DOWN), run_time=.2)
            
        init_array()
        # clone_up(new_scale=.7)
        # reposition(0, 1, 0.75, 0.8)

        self.wait(1)
        # clone_up(0.8)
        # # reposition(2, 3, 0.6, 0.7)
        # self.wait(1)

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


        reposition(0, 1, 0.75, 0.7)
        reposition(2, 3, 0.88, 0.7)
        reposition(4, 5, 0.65, 0.7)
        reposition(6, 7, 0.65, 0.7)

        # destroy_group()

        # low_array()
        delete_low_text()

        # move_text(UP)
        reposition(0, 2, 0.85, 0.7, move=False)
        self.play(self.texts[self.iter][2].animate.move_to(self.squares[self.iter-1][0]))
    
        
        reposition(0, 3, 0.9, 0.75, move=False)
        self.play(self.texts[self.iter][3].animate.move_to(self.squares[self.iter-1][1]))        
        
        self.play(self.texts[self.iter][0].animate.move_to(self.squares[self.iter-1][2]),
                  self.texts[self.iter][1].animate.move_to(self.squares[self.iter-1][3]))

        delete_squares(self.squares[self.iter][:4])
        temp0 = self.texts[self.iter][0]
        temp1 = self.texts[self.iter][1]
        self.texts[self.iter][0] = self.texts[self.iter][2]
        self.texts[self.iter][1] = self.texts[self.iter][3]
        self.texts[self.iter][2] = temp0
        self.texts[self.iter][3] = temp1


        reposition(4, 6, 0.75, 0.8, move=False)
        self.play(self.texts[self.iter][6].animate.move_to(self.squares[self.iter-1][4]))
        
        reposition(4, 7, 0.75, 0.8, move=False)
        self.play(self.texts[self.iter][7].animate.move_to(self.squares[self.iter-1][5]))
     
        self.play(self.texts[self.iter][4].animate.move_to(self.squares[self.iter-1][6]),
                  self.texts[self.iter][5].animate.move_to(self.squares[self.iter-1][7]))

        
        delete_squares( self.squares[self.iter][4:])
        self.iter -= 1
        self.texts[self.iter] = self.texts[self.iter+1]
        
        temp4 = self.texts[self.iter][4]
        temp5 = self.texts[self.iter][5]
        self.texts[self.iter][4] = self.texts[self.iter][6]
        self.texts[self.iter][5] = self.texts[self.iter][7]
        self.texts[self.iter][6] = temp4
        self.texts[self.iter][7] = temp5

        delete_low_text()

        reposition(0, 4, 0.85, 0.7, move=False)
        self.play(self.texts[self.iter][4].animate.move_to(self.squares[self.iter-1][0]))
        
        reposition(0, 5, 0.9, 0.75, move=False)        
        self.play(self.texts[self.iter][5].animate.move_to(self.squares[self.iter-1][1]))
        
        reposition(0, 6, 0.9, 0.75, move=False)
        self.play(self.texts[self.iter][6].animate.move_to(self.squares[self.iter-1][2]))

        reposition(0, 7, 0.9, 0.75, move=False)
        self.play(self.texts[self.iter][7].animate.move_to(self.squares[self.iter-1][3]))       
        
        
        self.play(self.texts[self.iter][0].animate.move_to(self.squares[self.iter-1][4]),
                   self.texts[self.iter][1].animate.move_to(self.squares[self.iter-1][5]),
                   self.texts[self.iter][2].animate.move_to(self.squares[self.iter-1][6]),
                   self.texts[self.iter][3].animate.move_to(self.squares[self.iter-1][7]))


        delete_squares(self.squares[self.iter])
        self.wait(2)