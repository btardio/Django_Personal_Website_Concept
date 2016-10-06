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

from django.contrib import admin
from app_manage_subscriptions.models import manage_subscriptions
from app_manage_subscriptions.forms import form_manage_subscriptions_model_form

# Register your models here.



class manage_subscriptions_admin(admin.ModelAdmin):

  list_display = ('time', 'email')

  readonly_fields = ('time',)

  form = form_manage_subscriptions_model_form

admin.site.register(manage_subscriptions, manage_subscriptions_admin)




