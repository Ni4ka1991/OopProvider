#!/usr/bin/env python3

from NumberProvider import NumberProvider

def positiveAction( number ):
    print( "Got an positive number >>> ", number )

provider = NumberProvider()
provider.whenPositive( positiveAction )
provider.start()

