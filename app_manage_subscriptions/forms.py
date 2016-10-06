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
from app_manage_subscriptions.models import manage_subscriptions
  
  
class form_manage_subscriptions_model_form(forms.ModelForm):

  email = forms.EmailField ( label = "Email", max_length = 100,
                             widget=forms.HiddenInput(attrs={'class': 'form-control'} ) )
      
  job_search_subscription = forms.BooleanField ( label = "Subscribe to job opening updates.",
                                                 required = False )
  
  weekly_newsletter_subscription = forms.BooleanField ( label = "Subscribe to weekly newsletter.",
                                                        required = False )
  
  deals_subscription = forms.BooleanField ( label = "Subscribe to receive deals and rebates.",
                                            required = False )
  
  announcements_subscription = forms.BooleanField ( label = "Subscribe to receive product and company announcements.",
                                                    required = False )

  
  class Meta:
    model = manage_subscriptions
    
    fields = (
              'email',
              'job_search_subscription',
              'weekly_newsletter_subscription',
              'deals_subscription',
              'announcements_subscription',)
        
    
    
    
class form_submit_email(forms.Form):

  email = forms.EmailField(label = "Email:", 
                           max_length = 100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  
  
  
