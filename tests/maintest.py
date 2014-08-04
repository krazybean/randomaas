#!/usr/bin/env python

import sys
import os
import unittest
import urllib2
sys.path.insert(0,os.path.abspath(__file__+"/../.."))
from app import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_randnum(self):
        m = main.randnum(6, 'num')
        self.assertTrue(bool(len(m) == 6))

    def test_response(self):
        r = urllib2.urlopen('http://localhost:9003')
        self.assertTrue(r.code == 200)

if __name__=='__main__':
    unittest.main()
