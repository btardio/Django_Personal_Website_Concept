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

from django import forms
from app_contact_form.models import contact_form  
  
  
class form_contact_form_model_form(forms.ModelForm):
  
  first_name = forms.CharField(label = "First Name:", 
			       max_length = 40, 
			       widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  middle_name = forms.CharField(label = "Middle Name:", 
				max_length = 40,
				widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  last_name = forms.CharField(label = "Last Name:", 
			      max_length = 40,
			      widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  email = forms.EmailField(label = "Email:", 
			   max_length = 100,
			   widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  comment = forms.CharField(label = "Comment:", 
			    max_length = 100000, 
			    widget=forms.Textarea(attrs={'class': 'form-control'}))
  
  class Meta:
    model = contact_form
    
    fields = ('first_name', 'middle_name', 'last_name', 'email', 'comment')
        
    