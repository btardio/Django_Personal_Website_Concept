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

"""cv_contact_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


#from app_contact_form import views
#from app_manage_subscriptions import views

#import app_contact_form
#import app_manage_subscriptions


#from app_contact_form.views import view_contact_form



urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'contact_form/', views.view_contact_form),
#    url(r'manage_subscriptions/', views.view_manage_subscriptions),
]



from app_contact_form import views

urlpatterns.append ( url(r'contact_form/', views.view_contact_form) )


from app_manage_subscriptions import views

urlpatterns.append ( url ( r'manage_subscriptions/(?P<email>([\w.+-]+@[\w-]+\.[\w\.-]+))', views.view_manage_subscriptions) )
urlpatterns.append ( url ( r'manage_subscriptions/', views.view_manage_subscriptions ) )

urlpatterns.append ( url ( r'submit_email/(?P<email>([\w.+-]+@[\w-]+\.[\w\.-]+))', views.view_submit_email ) )
urlpatterns.append ( url ( r'submit_email/', views.view_submit_email ) )


from app_opening_page import views

urlpatterns.append ( url ( r'^$', views.view_opening_page ) )
urlpatterns.append ( url ( r'^index.html/$', views.view_opening_page ) )



from app_resume_page import views

urlpatterns.append ( url ( r'resume/', views.view_resume_page ) )















