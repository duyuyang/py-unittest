import unittest
import dojo, requests
from mock import patch, Mock


class Testdojo(unittest.TestCase):

    @patch.object(dojo, 'bar')
    def test_foo_0_0(self, mock_bar):
        mock_bar.return_value = 8
        result = dojo.foo_0(5)
        self.assertEqual(-3, result)

    def test_foo_0_1(self):
        with patch.object(dojo, 'bar')\
            as mock_bar:
                mock_bar.return_value = 8
                result = dojo.foo_0(5)
                self.assertEqual(-3, result)

    @patch('dojo.bar')
    def test_foo_0_2(self, mock_bar):
        mock_bar.return_value = 8
        result = dojo.foo_0(5)
        self.assertEqual(-3, result)

    def test_foo_0_3(self):
        dojo.bar = Mock()
        dojo.bar.return_value = 8
        result = dojo.foo_0(5)
        self.assertEqual(-3, result)

    @patch.object(dojo, 'bar')
    @patch.object(dojo, 'something')
    def test_foo_1_0(self,
                     mock_something,
                     mock_bar):
        dojo.foo_1(14)
        self.assertEqual(mock_bar.call_count, 1)
        mock_bar.assert_called_once_with(14)
        mock_something.assert_not_called()

    @patch.object(dojo, 'parse_large_file')
    def test_foo_2_0(self, mock_file):
        mock_file.side_effect = MemoryError
        result = dojo.foo_2('something')
        self.assertEqual('Boom!', result)

    @patch.object(requests, 'get')
    def test_foo_3_0(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'it works'
        result = dojo.foo_3('http://localhost')
        self.assertEqual('it works', result)

    @patch.object(dojo, 'bar')
    def test_foo_4_0(self, mock_bar):
        mock_bar.return_value = 11
        self.assertRaises(Exception, lambda: dojo.foo_4(8))
