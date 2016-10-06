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

from django.test import TestCase
from django.test import Client
from app_manage_subscriptions.models import manage_subscriptions

# Create your tests here.



class app_manage_subscriptions_test_case ( TestCase ):
  
  def setUp(self):
    
    manage_subscriptions.objects.all().delete()
  
  
  def test_contact_form_submit ( self ):
    c = Client()
    self.assertEqual ( 1, 1 )
    
    
    # submit_email
    
    # .. get request
    
    response = c.get('/submit_email/')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>OhAQEyLYb5LK2ME10E750JSq3j67GfYd</UNIT_TEST_ID>', response.content.decode() )
    
     
    # .. get request with email in url with no db entry
     
    dbobj = manage_subscriptions.objects.filter ( email='b@b.com' )
    
    self.assertEqual ( len(dbobj), 0 )
    
    response = c.get('/submit_email/b@b.com')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter ( email='b@b.com' )
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, True )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, True )
    self.assertEqual ( dbobj.announcements_subscription, True )
    
    # .. get request after creation of db entry
    
    response = c.get('/submit_email/b@b.com')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter ( email='b@b.com' )
    
    self.assertEqual ( len(dbobj), 1 )

    
    # .. post request with no db entry
    
    dbobj = manage_subscriptions.objects.filter(email='d@d.com')
    
    self.assertEqual ( len(dbobj), 0 )
    
    response = c.post('/submit_email/', { 'email' : 'd@d.com' } )
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter(email='d@d.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, True )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, True )
    self.assertEqual ( dbobj.announcements_subscription, True )
    
    # .. post request after creation of db entry
    
    response = c.post('/submit_email/', { 'email' : 'd@d.com' } )
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter(email='d@d.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    
    # manage_subscriptions
    
    # .. get request
    
    response = c.get ( '/manage_subscriptions/', follow=True )
    
    self.assertEqual ( response.redirect_chain[0][1], 302 )
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>OhAQEyLYb5LK2ME10E750JSq3j67GfYd</UNIT_TEST_ID>', response.content.decode() )
    
    
    # .. get request with email in url

    dbobj = manage_subscriptions.objects.filter(email='c@c.com')
    
    self.assertEqual ( len(dbobj), 0 )
    
    response = c.get('/manage_subscriptions/c@c.com')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter(email='c@c.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, True )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, True )
    self.assertEqual ( dbobj.announcements_subscription, True )
    
    # .. get request after creation of db entry with email in url
    
    response = c.get('/manage_subscriptions/c@c.com')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter(email='c@c.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, True )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, True )
    self.assertEqual ( dbobj.announcements_subscription, True )
    
    # .. post request changes subscription choices
    
    response = c.post ( '/manage_subscriptions/', { 'email' : 'c@c.com',
                                                    'job_search_subscription' : False,
                                                    'weekly_newsletter_subscription' : False,
                                                    'deals_subscription' : False,
                                                    'announcements_subscription' : False } )
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( 'manage_subscriptions submission received.', response.content.decode() )    
    
    dbobj = manage_subscriptions.objects.filter(email='c@c.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, False )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, False )
    self.assertEqual ( dbobj.deals_subscription, False )
    self.assertEqual ( dbobj.announcements_subscription, False )   
    
    
    # .. post request without db entry and non default subscription choices
    
    dbobj = manage_subscriptions.objects.filter(email='a@a.com')
    
    self.assertEqual ( len(dbobj), 0 )
    
    response = c.post ( '/manage_subscriptions/', { 'email' : 'a@a.com',
                                                    'job_search_subscription' : False,
                                                    'weekly_newsletter_subscription' : True,
                                                    'deals_subscription' : False,
                                                    'announcements_subscription' : False } )
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( 'manage_subscriptions submission received.', response.content.decode() )    
    
    dbobj = manage_subscriptions.objects.filter(email='a@a.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, False )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, False )
    self.assertEqual ( dbobj.announcements_subscription, False )   
    
    # .. get request after creation of non default choices
    
    response = c.get('/manage_subscriptions/a@a.com')
    
    self.assertEqual ( response.status_code, 200 )
    
    self.assertIn ( '<UNIT_TEST_ID hidden>7wdfrNWdgU4LP0ZmKYRqRsH7KI04LbKA</UNIT_TEST_ID>', response.content.decode() )
    
    dbobj = manage_subscriptions.objects.filter(email='a@a.com')
    
    self.assertEqual ( len(dbobj), 1 )
    
    dbobj = dbobj[0]
    
    self.assertEqual ( dbobj.job_search_subscription, False )
    self.assertEqual ( dbobj.weekly_newsletter_subscription, True )
    self.assertEqual ( dbobj.deals_subscription, False )
    self.assertEqual ( dbobj.announcements_subscription, False )
    
    
    

    