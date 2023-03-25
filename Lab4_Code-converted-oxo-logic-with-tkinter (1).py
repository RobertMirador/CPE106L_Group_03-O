import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os, random
import oxo_data


class Game:
    def __init__(self):
        self.game = self.newGame()

    def select_file(self):
        target = filedialog.askopenfilename()
        with open( target ) as f:
            for line in f:
                print( line, end='' )

    def newGame(self):
        ' return new empty game'
        return list( " " * 9 )

    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame( self.game )

    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len( game ) == 9:
                self.game = game
            else:
                self.game = self.newGame()
        except IOError:
            self.game = self.newGame()

    def _generateMove(self):
        ''' generate a random cell from those available.
        If all cells are used return -1'''
        options = [i for i in range( len( self.game ) ) if self.game[i] == " "]
        if options:
            return random.choice( options )
        else:
            return -1

    def _isWinningMove(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.game[a] + self.game[b] + self.game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.game[cell] != ' ':
            raise ValueError( 'Invalid cell' )
        else:
            self.game[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.game[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        game = self.newGame()
        while not result:
            print( self.game )
            try:
                result = self.userMove( self._generateMove() )
            except ValueError:
                print( "Oops, that shouldn't happen" )
            if not result:
                result = self.computerMove()

            if not result:
                continue
            elif result == 'D':
                print( "Its a draw" )
            else:
                print( "Winner is:", result )
            print( self.game )


if __name__ == "__main__":
    game = Game()
    game.test()
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os, random
import oxo_data


class Game:
    def __init__(self):
        self.game = self.newGame()

    def select_file(self):
        target = filedialog.askopenfilename()
        with open( target ) as f:
            for line in f:
                print( line, end='' )

    def newGame(self):
        ' return new empty game'
        return list( " " * 9 )

    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame( self.game )

    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len( game ) == 9:
                self.game = game
            else:
                self.game = self.newGame()
        except IOError:
            self.game = self.newGame()

    def _generateMove(self):
        ''' generate a random cell from those available.
        If all cells are used return -1'''
        options = [i for i in range( len( self.game ) ) if self.game[i] == " "]
        if options:
            return random.choice( options )
        else:
            return -1

    def _isWinningMove(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.game[a] + self.game[b] + self.game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.game[cell] != ' ':
            raise ValueError( 'Invalid cell' )
        else:
            self.game[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.game[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        game = self.newGame()
        while not result:
            print( self.game )
            try:
                result = self.userMove( self._generateMove() )
            except ValueError:
                print( "Oops, that shouldn't happen" )
            if not result:
                result = self.computerMove()

            if not result:
                continue
            elif result == 'D':
                print( "Its a draw" )
            else:
                print( "Winner is:", result )
            print( self.game )


if __name__ == "__main__":
    game = Game()
    game.test()
