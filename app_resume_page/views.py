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

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from pudb import set_trace

# Create your views here.

def view_resume_page(request):
  
  #set_trace()
  
  renderedtemplates = ''
  
  # header 00 template
  template = loader.get_template('cv/header00.html')  
  context = { 'title': 'Resume' }
  renderedtemplates += template.render(context, request)
  
  template = loader.get_template('app_resume_page/resume_page.html')
  context = { }
  renderedtemplates += template.render(context, request)
  
  # footer 00 template
  template = loader.get_template('cv/footer00.html')
  context = { 'title': 'Resume' }  
  renderedtemplates += template.render(context, request)
  
  return HttpResponse(renderedtemplates)
