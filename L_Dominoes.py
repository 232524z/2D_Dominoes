import numpy as np
class L:
    table = None

    def __init__(self, dimx, dimy):
        self.table = np.array([[0 for i in range(dimx)] for j in range(dimy)])

    def __repr__(self):
        return str(self.table)

    @staticmethod
    def mex(options):
        for i in range(len(options)):
            try:
                options.index(i)
            except ValueError:
                return i
        return len(options)+1

    @staticmethod
    def nim_sum(nim1, nim2):
        nim1, nim2 = bin(nim1)[2:], bin(nim2)[2:]
        sum = 0
        length = max(len(nim1), len(nim2))
        for i in range(1,length+1):
            try:
                digit1 = int(nim1[-i])
            except:
                digit1 = 0

            try:
                digit2 = int(nim2[-i])
            except:
                digit2 = 0


            if digit1 != digit2:
                sum += 2**(i-1)
        return sum

    def get_table(self):
        return self.table

    def set_value(self, row, col, value):
        row, col = row-1, col-1
        self.table[row][col] = value
        try:
            self.table[col][row] = value
        except:
            pass

    def get_value(self, row, col):
        if row == 0 or col == 0:
            return 0
        return self.table[row-1][col-1]


    def find_options(self, height, width, index):
        if index+1 < height:
            up = self.get_value(width, height-(index+1))
            down = self.nim_sum(index, width-1)
            sideways = self.nim_sum(index, up)
            options = [up,down,sideways]
            return options
        if index+1 == height:
            up = width-1
            right = height-1
            out = self.nim_sum(width-1,height-1)
            options = [up,right,out]
            return options
        if index +1 > height:
            return self.find_options(width,height,((width+height-1)-index))