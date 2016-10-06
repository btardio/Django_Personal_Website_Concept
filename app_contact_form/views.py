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
from app_contact_form.forms import form_contact_form_model_form
from django.utils import timezone
from collections import deque

from pudb import set_trace

# Create your views here.

contact_submissions_deque = deque(maxlen=100)

def view_contact_form(request):
  
  #set_trace()
  
  renderedtemplates = ''
  status_success = True
  status_message = ''
  
  # header 00 template
  template = loader.get_template('cv/header00.html')  
  context = { 'title': 'Contact Form' }
  renderedtemplates += template.render(context, request)
  
  if request.method == 'POST':
    
    clientip = request.META['REMOTE_ADDR']
    
    contact_submissions_deque.append ( clientip )
    
    form = form_contact_form_model_form(request.POST)
        
    if form.is_valid():

      if ( contact_submissions_deque.count( clientip ) >= 10 ):
        status_success = False
        status_message = 'Your submission did not go through, you can only have 5 submissions.'
      
      else:
        status_success = True
        status_message = 'Your contact request has been received.'
        new_contact_form_submission = form.save()
        
  else:
    
    form = form_contact_form_model_form()
  
  template = loader.get_template('app_contact_form/contact_form.html')
  context = { 'form': form, 'status_success': status_success, 'status_message': status_message }
  renderedtemplates += template.render(context, request)
  
  
  # footer 00 template
  template = loader.get_template('cv/footer00.html')
  context = { 'title': 'Contact Form' }  
  renderedtemplates += template.render(context, request)

  
  return HttpResponse(renderedtemplates)
  
  