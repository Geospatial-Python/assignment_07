'''
Created on Mar 14, 2016

@author: Prad
'''
import random
import unittest
from point import Point

class TestFunctionalPointPattern(unittest.TestCase):
    def test_set_point(self):
        testPoint=Point(1,4)
        self.assertTrue(testPoint.x==1 and testPoint.y==4)
       
    def test_coincidence(self):
        testPoint=Point(1,4)
        self.assertTrue(testPoint.check_if_coincident((1,4)))
    
    def test_shift(self):
        testPoint=Point(1,4)
        shift_x=10
        shift_y=10
        testPoint.shift_point(shift_x,shift_y)
        self.assertEqual((testPoint.x,testPoint.y),(11,14))
        
    def test_mult(self):
        pt=Point(1,4)      
        pt=pt*5;
        self.assertEqual((pt.x,pt.y),(5,20))
    
    def test_add(self):
        pt=Point(1,4)
        pt=pt+10
        self.assertEqual((pt.x,pt.y),(11,14))
    
    def test_marked(self):
        mark_list=['mercury', 'venus', 'earth', 'mars']
        point_list=[]
        mer_count=0
        v_count=0
        e_count=0
        mar_count=0
        random.seed(43523)
        for i in range(1,20):
            curr_choice=random.choice(mark_list)
            point_list.append(Point(1,1,curr_choice))      
            if(curr_choice=='mercury'):
                mer_count+=1
            elif(curr_choice=='venus'):
                v_count+=1
            elif(curr_choice=='earth'):
                e_count+=1
            else:
                mar_count+=1
        mer_count_check=0
        v_count_check=0
        e_count_check=0
        mar_count_check=0
        
        for i in range(1,20):
            curr_mark=point_list.pop().mark
            if(curr_mark=='mercury'):
                mer_count_check+=1
            elif(curr_mark=='venus'):
                v_count_check+=1
            elif(curr_mark=='earth'):
                e_count_check+=1
            elif(curr_mark=='mars'):
                mar_count_check+=1
        
        self.assertEqual(mer_count,mer_count_check)
        self.assertEqual(v_count, v_count_check)
        self.assertEqual(e_count, e_count_check)
        self.assertEqual(mar_count,mar_count_check)
        