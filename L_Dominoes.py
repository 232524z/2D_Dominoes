class L:
    state = None

    def __init__(self, dimx, dimy):
        self.state = [[0 for i in range(dimx)] for j in range(dimy)]

    def __repr__(self):
        for row in self.state:
            print(row)