'''
Cerner Design Question:
Design Chess Board'''

import enum

class Board():

    def __init__(self):
        self.board = self.createboard()

    def createboard(self):
        self.board = [['X' for x in range(8)] for y in range(8)]
        return self.board

    def getboard(self):
        return self.board

class Pieces():
    def __init__(self,x,y,color,avail = True):
        try:
            self.x = x
            self.y = y
            if color not in (color.black,color.white):
                raise ValueError
            self.color = color
            self.avail = avail
            self.captives = []
        except ValueError:
            print('Pieces value incorrect')

    def validmove(self,board,fx,fy,tx,ty):
        if fx == tx and fy == ty:
            return False
        elif fx < 0 or fx > 7 or fy < 0 or fy > 7 or tx < 0 or tx > 7 or ty < 0 or ty > 7:
            return False
        else:
            return True

class King(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'King'
        self.kmoves = []

    def getpossmoves(self):
        self.kmoves.append((self.x + 1, self.y))
        self.kmoves.append((self.x - 1, self.y))
        self.kmoves.append((self.x, self.y + 1))
        self.kmoves.append((self.x, self.y - 1))
        self.kmoves.append((self.x + 1, self.y + 1))
        self.kmoves.append((self.x - 1, self.y - 1))
        self.kmoves.append((self.x + 1, self.y - 1))
        self.kmoves.append((self.x - 1, self.y + 1))


    def validmove(self,board,fx,fy,tx,ty):
        if (super(Pieces,self).validmove(board,fx,fy,tx,ty)) :
            if (tx,ty) in self.getpossmoves():
                if board[tx][ty] != 'X':
                    print('Captured : ', board[tx][ty])
                    self.captives.append(board[tx][ty])

                self.x = tx
                self.y = ty
            else:
                print('Invalid Move')
        else :
            print('Invalid Move')

'''
define possible moves and valid moves for rest of the pieces. 
'''
class Queen(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'Queen'
        self.qmoves = []
		
		
		

class Knight(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'Knight'
        self.nmoves = []

class Bishop(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'Bishop'
        self.bmoves = []

class Rook(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'Rook'
        self.rmoves = []

class Pawn(Pieces):

    def __init__(self,x,y,color,avail):
        Pieces.__init__(self,x,y,color,avail)
        self.type = 'Pawn'
        self.pmoves = []

class color(enum.Enum):
    black = 'black'
    white = 'white'

class Game():

    def __init__(self):
        self.temp = Board()
        self.board = self.temp.getboard()


    def placepieces(self):

        for i in range(8):
            self.board[1][i] = Pawn(1,i,color.White)
            self.board[6][i] = Pawn(6,i,color.Black)

        #white
        self.board[0][0] = Rook(0, 0, color.White)
        self.board[0][7] = Rook(0, 7, color.White)
        self.board[0][1] = Bishop(0, 1, color.White)
        self.board[0][6] = Bishop(0, 6, color.White)
        self.board[0][2] = Knight(0, 2, color.White)
        self.board[0][5] = Knight(0, 5, color.White)
        self.board[0][3] = King(0, 3, color.White)
        self.board[0][4] = Queen(0, 4, color.White)

        #black
        self.board[7][0] = Rook(7, 0, color.Black)
        self.board[7][7] = Rook(7, 7, color.Black)
        self.board[7][1] = Bishop(7, 1, color.Black)
        self.board[7][6] = Bishop(7, 6, color.Black)
        self.board[7][2] = Knight(7, 2, color.Black)
        self.board[7][5] = Knight(7, 5, color.Black)
        self.board[7][4] = King(7, 4, color.Black)
        self.board[7][3] = Queen(7, 3, color.Black)







































