import os
import sys
import unittest

import go_template
from go_template.utils import sha256sum


class TestMethods(unittest.TestCase):
    def test_add(self):
        test_dir = os.path.dirname(__file__)
        go_template.render_template(
            os.path.join(test_dir, 'sample.tmpl'),
            os.path.join(test_dir, 'values.yml'),
            os.path.join(test_dir, 'output.txt'))

        output_hash = sha256sum(os.path.join(test_dir, 'output.txt'))
        test_hash = sha256sum(os.path.join(test_dir, 'test.txt'))
        self.assertEqual(output_hash, test_hash)

if __name__ == '__main__':
    unittest.main()
