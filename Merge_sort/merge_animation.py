from manim import *
from numpy import array

class CreateVector(Scene):

    def construct(self):        
        divide_up = array((0.0, 1.5, 0.0))
        divide_upl = array((-.5, 1.0, 0.0))
        divide_upr = array((.5, 1.0, 0.0))

        def init_array():
            """#TODO

            """            

            squares = []
            texts = []

            offset = .5
            for i in range(0,5):
                square = Square()
                ft = Text(f"{5-i}", font="Comic Sans")
                square.set_fill(BLUE, opacity=0.5,).scale(.5)

                self.play(Create(VGroup(square, ft)), runtime = .5)

                self.play(square.animate.to_edge(DL).shift(RIGHT*i), 
                        ft.animate.to_edge(DL + offset).shift(RIGHT*i + offset+.04), 
                        run_time = .5)

                squares.append(square)
                texts.append(ft)
            
            self.squares = squares
            self.texts = texts


        def join_arr_group(group, new_scale, movement, displace, anim_time=.2):
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
                print(i, j)
                self.play(Create(i), run_time=anim_time)
                self.play(i.animate.shift(divide_up).scale(new_scale),  
                          j.animate.shift(divide_up).scale(new_scale),
                          run_time=anim_time)
                
                if last:
                    self.play(i.animate.next_to(last, movement + displace),  
                              j.animate.next_to(last, movement),
                              run_time=anim_time)
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

            self.squares = [i for (i,j) in group]
            self.texts = [j for (i,j) in group]

        def reposition(n1, n2, movr, movl):
            """Animates the shuffling of two elements in array

            Args:
                n1 (int): The left-most index to shuffle to the right
                n2 (int): The right-most index to shuffle to the right
            """            
            self.play(self.squares[n1].animate.set_fill(YELLOW),
                      self.squares[n2].animate.set_fill(YELLOW))

            self.play(self.texts[n1].animate.shift((movr * RIGHT)),
                    self.texts[n2].animate.shift(movl * LEFT))
    
            self.texts[n1], self.texts[n2] = self.texts[n2], self.texts[n1]

            self.play(self.squares[n1].animate.set_fill(BLUE),
                       self.squares[n2].animate.set_fill(BLUE))

            

        init_array()
        clone_up(new_scale=.7)
        self.wait(1)

        reposition(0,1, 0.75 , 0.8)
        clone_up(0.8)
        reposition(2,3, 0.6, 0.7)
        clone_up(new_scale=1)
        reposition(2, 4, 1, 1)
        reposition(3, 4 ,0.75, 0.8)
