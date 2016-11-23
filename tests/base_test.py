from __future__ import unicode_literals

import os
import unittest
import shutil

from tests.settings import BASE_DIR


class BaseTest(unittest.TestCase):

    maxDiff = None

    TEST_PROJECT_DIR = BASE_DIR
    TEST_APP_NAME = 'test-app'
    TEST_APP_DIR = os.path.join(TEST_PROJECT_DIR, TEST_APP_NAME)

    @classmethod
    def setUpClass(cls):
        os.makedirs(cls.TEST_PROJECT_DIR)
        os.makedirs(os.path.join(cls.TEST_PROJECT_DIR, cls.TEST_APP_NAME))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.TEST_PROJECT_DIR)
