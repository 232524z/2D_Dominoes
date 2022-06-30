from game import Game


class L(Game):

    def __init__(self, table_size):
        super().__init__(table_size)

    # Finds all the nim values that would result from toppling a specific domino in all possible directions
    def find_options(self, height, width, index):
        """
        :param height: height of the L
        :param width: width of the L
        :param index: the index of the domino in question. The domino at the top of the L has index 0, and indices
        increase as you move down and to the right on the domino.
        :return: an array of nim values that can be reached

        The directions calculated are the resulting nim values of toppling the domino in that direction

        Toppling a domino on an L can only yield some combinations of smaller Ls and lines of dominoes. The values of
        these shapes are known, so the game value is the nim sum of every component game
        """

        # If the domino is on the vertical stretch of the L
        if index + 1 < height:
            up = self.get_value(height - (index + 1), width)
            down = self.nim_sum(index, width - 1)
            out = self.nim_sum(index, up)
            options = [up, down, out]

        # If the domino is the corner piece of the L
        if index + 1 == height:
            up = width - 1
            right = height - 1
            out = self.nim_sum(height - 1, width - 1)
            options = [up, right, out]

        # If the domino is on the horizontal stretch of the L
        if index + 1 > height:
            dominoes_to_the_left = index - height + 1
            dominoes_to_the_right = width - dominoes_to_the_left - 1
            left = self.nim_sum(height - 1, dominoes_to_the_right)
            right = self.get_value(height, dominoes_to_the_left)
            out = self.nim_sum(right, dominoes_to_the_right)
            options = [left, right, out]

        return options
