# -*- coding: utf-8 -*-
"""

equilateral triangles have all three sides with the same length
isosceles triangles have two sides with the same length
scalene triangles have three sides with different lengths
right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2

program in Python to classify triangles and use an automated test platform, 
e.g. UnitTest or PyTest, and write test cases to test your implementation of classifying triangles.  
The goal is for you to gain experience using automated test tools 
and to think through the issues associated with testing a "system".  


@author: dagrawa2
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    elif a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == b**2+a**2: 
        return 'Right'
    elif a != b and a != c and b != c :
        return 'Scalene'
    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testPositiveClassifyTriangle(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,8),'Scalene','3,4,8 is a Scalene triangle')
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testNegativeClassifyTriangle(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        self.assertNotEqual(classifyTriangle(3,4,5),'Scalene','Should be Right')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(2,2,1)

    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
