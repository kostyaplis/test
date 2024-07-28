import unittest
import tempfile
import os
import sys

# Add parent dir to the sys.path, so we can import
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from process import get_top_lines

class TestGetTopLines(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with test data
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
        self.test_file.write("http://api.tech.com/item/111111 9\n")
        self.test_file.write("http://api.tech.com/item/222222 350\n")
        self.test_file.write("http://api.tech.com/item/333333 25\n")
        self.test_file.write("http://api.tech.com/item/444444 231\n")
        self.test_file.write("http://api.tech.com/item/555555 111\n")
        self.test_file.write("http://api.tech.com/item/666666 350\n")
        self.test_file.close()

    def tearDown(self):
        # Remove the temporary file
        os.remove(self.test_file.name)

    def test_get_top_lines(self):
        # Test the function to get the top 1 line
        expected_output = [
            "http://api.tech.com/item/222222",
        ]
        result = get_top_lines(self.test_file.name, 1)
        self.assertEqual(result, expected_output)

        # Test the function to get the top 2 lines
        expected_output = [
            "http://api.tech.com/item/222222",
            "http://api.tech.com/item/666666",
        ]
        result = get_top_lines(self.test_file.name, 2)
        self.assertEqual(result, expected_output)

        # Test the function to get the top 3 lines
        expected_output = [
            "http://api.tech.com/item/222222",
            "http://api.tech.com/item/666666",
            "http://api.tech.com/item/444444",
        ]
        result = get_top_lines(self.test_file.name, 3)
        self.assertEqual(result, expected_output)

        # Test the function to get the top 4 lines
        expected_output = [
            "http://api.tech.com/item/222222",
            "http://api.tech.com/item/666666",
            "http://api.tech.com/item/444444",
            "http://api.tech.com/item/555555",
        ]
        result = get_top_lines(self.test_file.name, 4)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()