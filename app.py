#!/usr/bin/env python3

from os import system
from NumberProvider import *

def positiveAction( number ):
    print( "Got an positive number >>> ", number )

def negativeAction( number ):
    print( "Got an negativ number >>>", number )

def action( number ):
    print( "Got a number >>> ", number )
try:
    provider = NumberProvider( -5, 200  )
    provider.whenPositive( positiveAction )
    provider.whenNegative( negativeAction )
    provider.start()
except:
    print( "You may have entered invalid data." )


