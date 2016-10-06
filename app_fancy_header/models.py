#
#    
#
#    Copyright (C) 2016 Brandon C Tardio
#
#    This file is part of DPWC
#
#    DPWC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DPWC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DPWC.  If not, see <http://www.gnu.org/licenses/>.
#    
#    Contact: BTardio@gmail.com
#             818 424 6838
#
#
#    Django_Personal_Website_Concept ( DPWC )
#
#
#

from django.db import models
from django.utils import safestring
import random
#import numpy
# Create your models here.

class point():
  
  x = 0
  y = 0

class fancy_header():
  
  @staticmethod
  def gen_fancy_header():
    
    
    width = 800
    height = 100
    
    rvar = ''
    
    #for i in range(0,5):
    #  rvar += '%d' % random.randint(-100, 100)
    #  rvar += '%d' % random.randint(-100, 100)
    
    rvar += '<svg width="%d" height="%d">' % (width, height)
    
    iterrangex = 12
    iterrangey = 4
    
    widthdivision = width / iterrangex
    heightdivision = height / iterrangey
    
    
    widthdiff = int ( widthdivision / 2 )
    heightdiff = int ( heightdivision / 2 )

    array = []
    
    for x in range ( 0, iterrangex ):
      temparray = []
      for y in range ( 0, iterrangey ):
        temparray.append( point() )
      array.append(temparray)

    
    for x in range ( 0, iterrangex ):
      for y in range ( 0, iterrangey ):
        
        array[x][y] = point()
        array[x][y].x = (widthdivision * x) + random.randint ( 0, widthdiff )
        array[x][y].y = (heightdivision * y)
        #array[x][y].y = (heightdivision * y) + random.randint ( 0, heightdiff )
        
        
    for x in range(2, iterrangex-1):
      for y in range(2, iterrangey-1):
        rvar += '<polygon points="'
        
        xindex = x
        yindex = y
        
        # top left
        randomnum = random.randint ( 0, 1 )
        if ( randomnum == 0 and x != 1 and y != 1):
          rvar += '%d' % array[x-2][y-1].x
          rvar += ',' 
          rvar += '%d' % array[x-2][y-1].y

        else:
          rvar += '%d' % array[x-1][y-1].x
          rvar += ',' 
          rvar += '%d' % array[x-1][y-1].y
          
        
        rvar += ' '
        
        # bottom left
        randomnum = random.randint ( 0, 1 )
        if ( randomnum == 0 and x != 1 and y != 1):
          rvar += '%d' % array[x-2][y].x
          rvar += ','
          rvar += '%d' % array[x-2][y].y
        
        else:
          rvar += '%d' % array[x-1][y].x
          rvar += ','
          rvar += '%d' % array[x-1][y].y
        
        rvar += ' '
        
        # bottom right
        randomnum = random.randint ( 0, 1 )
        if ( randomnum == 0 and x != 1 and y != 1):
          rvar += '%d' % array[x+1][y].x
          rvar += ','
          rvar += '%d' % array[x+1][y].y
        
        else:
          rvar += '%d' % array[x][y].x
          rvar += ','
          rvar += '%d' % array[x][y].y
        
        rvar += ' '

        # top right
        randomnum = random.randint ( 0, 1 )
        if ( randomnum == 0 and x != 1 and y != 1):
          rvar += '%d' % array[x+1][y-1].x
          rvar += ','
          rvar += '%d' % array[x+1][y-1].y

        else:
          rvar += '%d' % array[x][y-1].x
          rvar += ','
          rvar += '%d' % array[x][y-1].y
          
        
        #rvar += ' '
        #rvar += '%d,%d' % (
        rvar += '" style="fill:lime;stroke:black;stroke-width:1;stroke-opacity:0.5;fill-opacity:0.5;" />'
    
    
    
    
    
    rvar += '</svg>'
    
    return safestring.mark_safe(rvar)
  
    #return ''
  
  