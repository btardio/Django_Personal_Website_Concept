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

# Create your models here.


class manage_subscriptions ( models.Model ):
  
  time = models.DateTimeField ( auto_now = True )
  
  email = models.EmailField ( max_length = 100, unique = True )
  
  job_search_subscription = models.BooleanField ( default = True )
  
  weekly_newsletter_subscription = models.BooleanField ( default = True )
  
  deals_subscription = models.BooleanField ( default = True )
  
  announcements_subscription = models.BooleanField ( default = True )
  
  