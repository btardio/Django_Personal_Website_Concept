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

from app_contact_form.models import contact_form

# Create your tests here.


class app_contact_form_test_case ( TestCase ):
  
  def setUp(self):
    
    contact_form.objects.all().delete()
    
  
  
  def test_contact_form_submit ( self ):
    c = Client()
    
    
    # get request
    
    response = c.get('/contact_form/')
    
    self.assertEqual ( response.status_code, 200 )
    self.assertIn ( '<UNIT_TEST_ID hidden>BVGtdojgCes0foNZZ2b4a3EUs6UN7mtT</UNIT_TEST_ID>', response.content.decode() )
    
    # post request
    
    dbobj = contact_form.objects.filter ( first_name = 'john',
                                                  middle_name = 'smith',
                                                  last_name = 'beck',
                                                  email = 'jbeck@email.com',
                                                  comment = 'This is the comment.' )
    
    self.assertEqual ( len(dbobj), 0 )

    
    response = c.post('/contact_form/', {'first_name': 'john', 
                                         'middle_name': 'smith', 
                                         'last_name': 'beck',
					 'email': 'jbeck@email.com', 
					 'comment': 'This is the comment.'})

    dbobj = contact_form.objects.filter ( first_name = 'john',
                                                  middle_name = 'smith',
                                                  last_name = 'beck',
                                                  email = 'jbeck@email.com',
                                                  comment = 'This is the comment.' )
    
    self.assertEqual ( len(dbobj), 1 )
    self.assertEqual ( response.status_code, 200 )
    self.assertIn ( '<UNIT_TEST_ID hidden>BVGtdojgCes0foNZZ2b4a3EUs6UN7mtT</UNIT_TEST_ID>', response.content.decode() )
    self.assertIn ( 'Your contact request has been received.', response.content.decode() )
    
    # multiple post requests from same ip
    for i in range ( 2, 10 ) :
      
      response = c.post('/contact_form/', {'first_name': 'john', 
                                          'middle_name': 'smith', 
                                          'last_name': 'beck',
                                          'email': 'jbeck@email.com', 
                                          'comment': 'This is the comment.'})

      dbobj = contact_form.objects.filter ( first_name = 'john',
                                                    middle_name = 'smith',
                                                    last_name = 'beck',
                                                    email = 'jbeck@email.com',
                                                    comment = 'This is the comment.' )
      
      self.assertEqual ( len(dbobj), i )      
      self.assertEqual ( response.status_code, 200 )
      self.assertIn ( '<UNIT_TEST_ID hidden>BVGtdojgCes0foNZZ2b4a3EUs6UN7mtT</UNIT_TEST_ID>', response.content.decode() )
      self.assertIn ( 'Your contact request has been received.', response.content.decode() )

    # number of contact submissions is hard coded to <= 10 per ip, shouldn't submit beyond this
    for i in range ( 0, 10 ) :
        
      response = c.post('/contact_form/', {'first_name': 'john', 
                                          'middle_name': 'smith', 
                                          'last_name': 'beck',
                                          'email': 'jbeck@email.com', 
                                          'comment': 'This is the comment.'})

      dbobj = contact_form.objects.filter ( first_name = 'john',
                                                    middle_name = 'smith',
                                                    last_name = 'beck',
                                                    email = 'jbeck@email.com',
                                                    comment = 'This is the comment.' )
      
      self.assertEqual ( len(dbobj), 9 )
      self.assertEqual ( response.status_code, 200 )
      self.assertIn ( '<UNIT_TEST_ID hidden>BVGtdojgCes0foNZZ2b4a3EUs6UN7mtT</UNIT_TEST_ID>', response.content.decode() )
      self.assertIn ( 'Your submission did not go through, you can only have', response.content.decode() )
    
    