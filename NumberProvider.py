# NumberProvider.py
from os import system
from random import randint
from time import sleep

class NumberProvider:
    def __init__( self, min = -100, max = 100 ):
        if( type(min) == int and type(max) == int ):
            self.min = min
            self.max = max
        else:
            print( "Index cannot be something else than an integer!" )
            input( "Hit ENTER to continue ..." )

    def generate( self ):
        return randint( self.min, self.max )

    def whenPositive( self, positiveCB ):
        self.positiveCB = positiveCB

    def whenNegative( self, negativCB ):
        self.negativCB = negativCB

    def start( self ):
        system( "clear" )
        while True:
            number = self.generate()
            if( number  >= 0 ):
                self.positiveCB( number )
            else:
                self.negativCB( number )
            sleep( 1 ) 
