'''
Created on Jan 30, 2010

@author: changwang
'''
import unittest

from edu.wmich.hopfield.MindofHomer import dec2bin, state_factory, matrix_creator, state2string
from edu.wmich.hopfield.main import prune_input

class MindofHomerTest(unittest.TestCase):
    """ Unittest for core functions. """
    
    def testDec2Bin(self):
        self.assertEqual('1000001', dec2bin(65)) # 'A'
        self.assertEqual('1100001', dec2bin(97)) # 'a'
        
        self.assertEqual('1000010', dec2bin(66)) # 'B'
        self.assertEqual('1100010', dec2bin(98)) # 'b'
        
        self.assertEqual('1011010', dec2bin(90)) # 'Z'
        self.assertEqual('1111010', dec2bin(122)) # 'z'
        
        self.assertEqual('0100000', dec2bin(32)) # 'space'
        self.assertEqual('0101100', dec2bin(44)) # ','
        self.assertEqual('0101110', dec2bin(46)) # '.'
        
        self.assertEqual('0000001', dec2bin(1)) # '1'
        self.assertEqual('0001001', dec2bin(9)) # '9'
    
    def testStableStateLength(self):
        self.assertEqual(70, len(state_factory('helloworld')))

    def testStableStateContent(self):
        stable_state = state_factory('hello world!')
        for ch in stable_state:
            self.assert_(ch in [0, 1])
    
    def testMatrixCreator(self):
        self.assertEqual(70, len(matrix_creator(state_factory('helloworld'))))
        
    def testPruneInput(self):
        self.assertEqual(10, len(prune_input('helloworld!')))
        self.assertEqual(10, len(prune_input('chang')))
        
    def testState2String(self):
        self.assertEqual('A', state2string([1, 0, 0, 0, 0, 0, 1]))
        self.assertEqual('a', state2string([1, 1, 0, 0, 0, 0, 1]))
        
        self.assertEqual('B', state2string([1, 0, 0, 0, 0, 1, 0]))
        self.assertEqual('b', state2string([1, 1, 0, 0, 0, 1, 0]))
        
        self.assertEqual('Z', state2string([1, 0, 1, 1, 0, 1, 0]))
        self.assertEqual('z', state2string([1, 1, 1, 1, 0, 1, 0]))
        
        self.assertEqual(' ', state2string([0, 1, 0, 0, 0, 0, 0]))
        
        self.assertEqual('1', state2string([0, 0, 0, 0, 0, 0, 1]))

if __name__ == "__main__":
    unittest.main()