import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.expanduser(__file__ + '/../..')))

import project_template_python


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(project_template_python.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
