"""--------------------------------------------------------------------------
This is a game of players and enemies played on a 2D board of 64 squares
done as a bose to play chess
--------------------------------------------------------------------------"""
#============================================================================
#CHESS BOARD
#============================================================================
from random import *
seed()
#----------------------------------------------------------------------------
COL = ['a','b','c','d','e','f','g','h']
def Convert(LOC):
    r = int(LOC[1])
    c = COL.index(LOC[0]) + 1
    return r,c

def Revert(Tuple):
    return str(COL[Tuple[1]-1])+str(Tuple[0])
#----------------------------------------------------------------------------
class Piece:
    C = '-'
    Loc = (0,0)
    def __init__(self, c, l):
        self.C = c
        self.Loc = Convert(l)

    def __str__(self):
        return Revert(self.Loc)+":"+self.C

    def setC(self, C):
        self.C = c

    def getC(self):
        return self.C

    def setLoc(self,N_Loc):
        self.Loc = N_Loc

    def getLoc(self):
        return (self.Loc)

#----------------------------------------------------------------------------

class King(Piece):
    no = int()
    def __init__(self, c, l, n):
            self.C = c
            self.Loc = Convert(l)
            self.no = n
    

    def __str__(self):
        if self.no < 10:
            return self.C+"K"+str(self.no)+"  "
        else:
            return self.C+"K"+str(self.no)+" "
        
    def Move(self,Cell):
        C_Loc = (self.getLoc())
        N_Loc = Convert(Cell.getId())        
        if(C_Loc[0] + 1 == N_Loc[0]) or (C_Loc[0] - 1 == N_Loc[0] or C_Loc[0] == N_Loc[0]):
            if(C_Loc[1] + 1 == N_Loc[1]) or (C_Loc[1] - 1 == N_Loc[1] or C_Loc[1] == N_Loc[1]):
                if not(Cell.Occupied):
                    self.setLoc(N_Loc)
                    return 1
                elif (Cell.getPiece().getC() != self.getC()):
                    self.setLoc(N_Loc)
                    return 2
                else:
                    return 3
        return 0


#----------------------------------------------------------------------------
class cell:
    Id = '--'
    Colour = '-'
    P = "     "
    Occupied = False
    def __init__(self,ID = '--',C = '-'):
        self.Id = ID
        self.Colour = C

    def __str__(self):
        return str("|" +self.Id + ":" + self.Colour + ":" + str(self.P) +"|")

    def __lt__(self,other):
        return self.Id < other.Id

    def getColour(self):
        return self.Colour

##    def setPiece(self,C,P):
##        self.P = (C,P)

    def getPiece(self):
        return self.P

    def getId(self):
        return self.Id

    def isOccupied(self):
        return self.Occupied

#----------------------------------------------------------------------------

class board:
    Pieces = {}
    def __init__(self):
        self.Board = {}
        for i in range(1,9):
            ind = 1
            if i % 2 == 0:
                ind = -1
            for j in ['a','b','c','d','e','f','g','h']:
                key = j+str(i)
                c = ["B","W"]
                self.Board[key] = cell(key,c[::ind][0],)
                ind *= -1

    def __str__(self):
        string = []
        for key in self.Board:
            string.append(self.Board[key])
        string.sort()
        fstr = ""
        for i in range(64):
            fstr += str(string[i])
            if (i+1)%8 == 0:
                fstr += "\n"
        return fstr 

    def getBoard(self):
        return self.Board

    
#============================================================================
#GAME 1
#============================================================================

def Play():
    game1 = board()
    print(game1)
    WN = int(input("Enter number of player's PIECES : "))
    print("All PLAYERS ARE WHITE (W)")
    BN = int(input("Enter number of Enemy PIECES: "))
    print("All Enimies are BLACK (B)")
    print("Placing ENEMIES ........")

    for i in range(1,BN + 1):
        st_cell = Revert((randint(1,8),randint(1,8)))
        game1.Board[st_cell].P = King('B',st_cell,i)
        game1.Board[st_cell].Occupied = True

    print(game1)
    flag = True
    while flag:
        l = range(1,WN + 1)
        for i in l:
            st_cell = input("Enter the starting cell of PLAYER "+str(i)+" : ")
            if st_cell not in game1.Board.keys():
                i = l[l.index(i) - 1]
                continue
            if(game1.Board[st_cell].isOccupied()):
                print("You cannot place on an OCCUPIED cell!")
                print("Re-enter starting cells")
                break
            game1.Board[st_cell].P = King('W',st_cell,i)
            game1.Board[st_cell].Occupied = True
            print(game1)
        flag = False

    flag = True
    print("Game Ends when all Enimies are eliminated!!")
    print("LETS PLAY!!")
    while flag:
        #player moves
        CL = input("Enter the cell of your PIECE : ")
        CL_int = Convert(CL)
        CL = Revert(CL_int)
        if not(CL_int[0] > 0 and CL_int[0] < 9 and CL_int[1] > 0 and CL_int[1] < 9):
            print("The cell entered does not exist on the board")
            continue
        if not(type(game1.Board[CL].P) != str and (game1.Board[CL].P.getC() == 'W')):
            print("Select cell with your PIECE")
            continue
        NL = input("Enter the new cell : ")
        NL_int = Convert(NL)
        NL = Revert(NL_int)
        #PLAYER MAKING THE MOVE
        if(NL_int[0] > 0 and NL_int[0] < 9 and NL_int[1] > 0 and NL_int[1] < 9):
            movFlag = game1.Board[CL].P.Move(game1.Board[NL])
        else:
            print("The cell entered does not exist on the board")
            continue
        if movFlag == 0:
            print("This move is not allowed")
        elif movFlag == 3:
            print("The destination is occupied by an ALLY")
        elif movFlag == 1:
            game1.Board[NL].P = game1.Board[CL].P
            game1.Board[NL].Occupied = True
            game1.Board[CL].P = "     "
            game1.Board[CL].Occupied = False
        elif movFlag == 2:
            game1.Board[NL].P = game1.Board[CL].P
            game1.Board[NL].Occupied = True
            game1.Board[CL].P = "     "
            game1.Board[CL].Occupied = False
            print("ONE ENEMY KILLED")
            BN -= 1
            if BN == 0:
                break

        print(game1)

        #Enemy moves
        Blist = []
        for cell in game1.Board:
            if type(game1.Board[cell].P) != str:
                if game1.Board[cell].P.getC() == 'B':
                    Blist.append(cell)
        ind = randint(0,len(Blist) - 1)
        CL = Blist[ind]
        movFlag = -1

        while movFlag != 1 and movFlag != 2:
            seed()
            NL = Revert((randint(1,8),randint(1,8)))
            NL_int = Convert(NL)

            #Making the move
            if(NL_int[0] > 0 and NL_int[0] < 9 and NL_int[1] > 0 and NL_int[1] < 9):
                movFlag = game1.Board[CL].P.Move(game1.Board[NL])
            else:
                print("The cell entered does not exist on the board")
                continue
            if movFlag == 0:
                continue
                #print("This move is not allowed")
            elif movFlag == 3:
                continue
                #print("The destination is occupied by an ALLY")
            elif movFlag == 1:
                game1.Board[NL].P = game1.Board[CL].P
                game1.Board[NL].Occupied = True
                game1.Board[CL].P = "     "
                game1.Board[CL].Occupied = False
            elif movFlag == 2:
                game1.Board[NL].P = game1.Board[CL].P
                game1.Board[NL].Occupied = True
                game1.Board[CL].P = "     "
                game1.Board[CL].Occupied = False
                print("ONE PLAYER KILLED")
                WN -= 1

        print(game1)
        if WN == 0:
            break
            
    #OUTSIDE THE WHILE LOOP
    if BN == 0:
        print("VICTORY!!!!")
    if WN == 0:
        print("YOU WERE KILLED")
            
#--------------------------------FUNCTION CALL-------------------------------
Play()
    

