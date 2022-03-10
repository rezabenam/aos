import unittest
import aos_locators as locators
import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.log_out()
        methods.log_in()
        methods.logger('created')
        methods.log_out()
        methods.tearDown()
