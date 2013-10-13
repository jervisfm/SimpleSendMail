
import unittest
import ssm


__author__ = 'Jervis Muindi'

class SSMTest(unittest.TestCase):
    def test_quick_validate_email(self):
        self.assertTrue(ssm.quick_validate_email('who@example.org'))
        self.assertFalse(ssm.quick_validate_email('bad@@example.rog'))



if '__main__' == __name__:
    unittest.main()
