# -*- coding: utf-8 -*-
'''
Copyright © 2017 DELL Inc. or its subsidiaries.  All Rights Reserved.
Created on May 4, 2017

@author: Michael Regert, Michael Hepfer
'''
import json
import unittest
import sys
import os
import logging
run_dir=os.path.abspath(os.path.dirname(__file__))
current_dir = os.getcwd()
os.chdir(run_dir)
sys.path.insert(0,os.path.abspath('../utility'))
sys.path.append(os.path.abspath('../handlers'))

from UtilBase import Utility
from VirtualIdentityMicroservice import VirtualIdentityHandler

logger = logging.getLogger(__name__)

class VirtualIdentityTest(unittest.TestCase):
    global networkId
    networkId = 0
    networkJson = ""

    def setUp(self):
        print("")

    ########################################################################
    # Test that Get Virtual Identities returns an empty list when empty
    def test001_GetVirtualIdentitiesEmpty(self):
        try:
            response = VirtualIdentityHandler().getVirtualIdentities()
            logger.info("Response Status Code: " + str(response.status_code))
            self.assertEqual(response.status_code, 200, "Response code should equal 200")

            logger.info("Response Text: " + response.text)
            responseJson = json.loads(response.text)
            #assert here
            self.assertEqual(responseJson["pagination"]["total"], 0, "Pagination total count should be 0")
            self.assertEqual(responseJson["pages"]["total"], 0, "Pages total count should be 0")

        except Exception as e1:
            logger.error("Exception: " + str(e1))
            raise e1



if __name__=="__main__":
    if len(sys.argv) > 1:
        VirtualIdentityHandler.host = sys.argv.pop()
    else:
        VirtualIdentityHandler.host = "http://localhost:46015"

    from test_manager import run_tests
    run_tests('VID')