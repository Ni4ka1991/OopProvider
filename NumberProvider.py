# NumberProvider.py

from random import randint
from time import sleep

class NumberProvider:
    def __init__( self, min = -100, max = 100 ):
        if( type(min) == int and type(max) == int):
            self.min = min
            self.max = max
        else:
            print( "Type error" )

    def generate( self ):
        return randint( self.min, self.max )

    def whenPositive( self, positiveCB ):
        self.positiveCB = positiveCB

    def whenNegative( self ):
        #2. ???
        pass

    def start( self ):
        while True:
            number = self.generate()
            if( number  >= 0 ):
                self.positiveCB( number )
            # 2. ???
            sleep( 1 ) 
