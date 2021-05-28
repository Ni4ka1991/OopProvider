# NumberProvider.py
from os import system
from random import randint
from time import sleep

class NumberProvider:
    def __init__( self, min = -100, max = 100 ):
        self.min = min
        self.max = max

    def generate( self ):
        return randint( self.min, self.max )

#    def whenPositive( self, positiveCB ):
#        self.positiveCB = positiveCB

#    def whenNegative( self, negativCB ):
#        self.negativ = negativCB
#        pass

    def start( self ):
        system( "clear" )
        while True:
            number = self.generate()
#            print( number )
#            if( number  >= 0 ):
#                self.positiveCB( number )
#            else:
#                self.negativCB( number )
            sleep( 1 ) 
