#!/usr/bin/env python

import sys
import os
import unittest
sys.path.insert(0,os.path.abspath(__file__+"/../.."))
from app import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_randnum(self):
        m = main.randnum(6, 'num')
        self.assertTrue(bool(len(m) == 6))

if __name__=='__main__':
    unittest.main()
