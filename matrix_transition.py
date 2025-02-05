from manim import *

class MatrixTransition(Scene):
    def construct(self):
        # Create a matrix and a text
        row_matrix = Matrix([[1, 2, 3, 4]])
        column_matrix = Matrix([[1], [2], [3], [4]])

        # Position the row matrix
        row_matrix.shift(UP)

        # Text for explanation (with a font that supports Vietnamese)
        row_text = Text("Ma trận dòng: m = 1", font="Arial", font_size=24).next_to(row_matrix, DOWN)
        column_text = Text("Ma trận cột: n = 1", font="Arial", font_size=24).next_to(column_matrix, RIGHT)

        # Display the row matrix and explanation text
        self.play(Write(row_matrix), Write(row_text))
        self.wait(1)

        # Transform the row matrix to the column matrix
        self.play(Transform(row_matrix, column_matrix), Transform(row_text, column_text))
        self.wait(1)
