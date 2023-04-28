from manim import *


class CreateVector(Scene):

    def construct(self):

        def init_array():
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

        def clone_up():
            squares_new = [i.copy() for i in self.squares] # Copies individual items
            texts_new = [i.copy() for i in self.texts]
        
            for i, j in zip(squares_new, texts_new):
                self.play(Create(i), run_time=.2)
                self.play(i.animate.shift(UP),  
                        j.animate.shift(UP),
                        run_time=.2)

            self.squares = squares_new
            self.texts = texts_new

        def reposition(n1, n2):
            self.play(self.squares[n1].animate.set_fill(YELLOW),
                      self.squares[n2].animate.set_fill(YELLOW))

            self.play(self.texts[n1].animate.shift(RIGHT),
                    self.texts[n2].animate.shift(LEFT))
    
            self.texts[n1], self.texts[n2] = self.texts[n2], self.texts[n1]

            self.play(self.squares[n1].animate.set_fill(BLUE),
                      self.squares[n2].animate.set_fill(BLUE))
            

        init_array()
        clone_up()

        reposition(0,1)
        clone_up()
        reposition(2,3)






class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))