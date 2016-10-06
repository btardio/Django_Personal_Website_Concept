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
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from app_manage_subscriptions.forms import form_manage_subscriptions_model_form, form_submit_email
from django.utils import timezone
from app_manage_subscriptions.models import manage_subscriptions

from pudb import set_trace

# Create your views here.







def db_object_from_email ( email ):
  dbentry = manage_subscriptions.objects.filter ( email = email )
  
  if ( len ( dbentry ) > 0 ):
    dbentry = dbentry[0]

  else:
    dbentry = manage_subscriptions ( email = email )
    dbentry.save()

  return dbentry




def view_manage_subscriptions(request, email='blank', dbentry=None):

  #set_trace()
  
  renderedtemplates = ''
  
  # header 00 template
  template = loader.get_template('cv/header00.html')  
  context = { 'title': 'Manage Subscriptions' }
  renderedtemplates += template.render(context, request)


  if ( dbentry != None ):
    form = form_manage_subscriptions_model_form(instance = dbentry)
    template = loader.get_template('app_manage_subscriptions/manage_subscriptions.html')
    context = { 'id': dbentry.id, 'form': form }
  
  elif request.method == 'POST':
    
    dbentry = manage_subscriptions.objects.filter ( email = request.POST['email'] )
    
    if ( len ( dbentry ) == 0 ):
      
      dbentry = db_object_from_email ( request.POST['email'] )
    
    else:
      
      dbentry = dbentry[0]
    
    form = form_manage_subscriptions_model_form(request.POST, instance = dbentry)
        
    if form.is_valid():      
      
      new_manage_subscriptions_submission = form.save()
      
      return HttpResponse("manage_subscriptions submission received.")
  

  elif ( email != 'blank' ):
    dbentry = db_object_from_email ( email )
    form = form_manage_subscriptions_model_form(instance = dbentry)
    template = loader.get_template('app_manage_subscriptions/manage_subscriptions.html')
    context = { 'id': dbentry.id, 'form': form }
    
    
  else:
    
    return HttpResponseRedirect('/submit_email/')
    

  # middle template
  
  renderedtemplates += template.render(context, request)
  
  
  # footer 00 template
  template = loader.get_template('cv/footer00.html')
  
  context = { 'title': 'Manage Subscriptions' }
  
  renderedtemplates += template.render(context, request)
  
  return HttpResponse(renderedtemplates)
  
  #return HttpResponse("view_contact_form")
  
  



def view_submit_email(request, email='blank', dbentry = None):
  
  #set_trace()
  
  renderedtemplates = ''
  
  # header 00 template
  template = loader.get_template('cv/header00.html')  
  context = { 'title': 'Manage Subscriptions' }
  renderedtemplates += template.render(context, request)

  if ( email != 'blank' ):
    
    dbentry = db_object_from_email ( email )
        
    return view_manage_subscriptions ( request, dbentry.email, dbentry )

  elif ( request.method == 'POST' ):

    form = form_submit_email(request.POST)
    
    if ( form.is_valid() ):
      
      dbentry = db_object_from_email ( form.cleaned_data['email'] )
      
      return view_manage_subscriptions ( request, dbentry.email, dbentry )
    
  else:

    form = form_submit_email()
    template = loader.get_template('app_manage_subscriptions/submit_email.html')
    context = { 'form': form }

  # middle template
  renderedtemplates += template.render(context, request)
  
  # footer 00 template
  template = loader.get_template('cv/footer00.html')
  
  context = { 'title': 'Manage Subscriptions' }
  
  renderedtemplates += template.render(context, request)
  
  return HttpResponse(renderedtemplates)


