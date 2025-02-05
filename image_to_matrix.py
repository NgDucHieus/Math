from manim import *

class ImageToMatrix(Scene):
    def construct(self):
        # Define the grayscale image as a grid of squares
        rows, cols = 8, 8  # Reduced number of rows and columns for resizing
        square_size = 0.7  # Adjusted size of each square
        max_value = rows * cols - 1  # Maximum grayscale value based on grid size
        grayscale_values = [[i * cols + j for j in range(cols)] for i in range(rows)]

        # Create the grid of squares
        squares = VGroup()
        for i in range(rows):
            for j in range(cols):
                color = interpolate_color(BLACK, WHITE, grayscale_values[i][j] / max_value)
                square = Square(side_length=square_size, color=color, fill_opacity=1)
                square.move_to(np.array([(j - cols / 2) * square_size, (rows / 2 - i) * square_size, 0]))
                squares.add(square)

        # Create the corresponding matrix values
        matrix_values = VGroup()
        for i in range(rows):
            for j in range(cols):
                value = Text(str(grayscale_values[i][j]), font_size=24)  # Adjust font size
                value.move_to(np.array([(j - cols / 2) * square_size, (rows / 2 - i) * square_size, 0]))
                matrix_values.add(value)

        # Show the grayscale image
        self.play(FadeIn(squares))
        self.wait(2)

        # Flip each square to reveal the matrix values
        animations = []
        for square, value in zip(squares, matrix_values):
            animations.append(Transform(square, value))

        self.play(*animations, run_time=4)
        self.wait(2)
