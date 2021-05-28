#!/usr/bin/env python3

from os import system
from NumberProvider import NumberProvider

def positiveAction( number ):
    print( "Got an positive number >>> ", number )

def negativeAction( number ):
    print( "Got an negativ number >>>", number )

def action( number ):
    print( "Got a number >>> ", number )

provider = NumberProvider( -10, 15  )
#provider.whenPositive( positiveAction )
#provider.whenNegative( negativeAction )
provider.start()
#print( number )

