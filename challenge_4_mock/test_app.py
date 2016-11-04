import unittest
import app, requests
from mock import patch, Mock


class TestApp(unittest.TestCase):

    @patch.object(app, 'bar')
    def test_foo_0_0(self, mock_bar):
        mock_bar.return_value = 8
        result = app.foo_0(5)
        self.assertEqual(-3, result)

    def test_foo_0_1(self):
        with patch.object(app, 'bar')\
            as mock_bar:
                mock_bar.return_value = 8
                result = app.foo_0(5)
                self.assertEqual(-3, result)

    @patch('app.bar')
    def test_foo_0_2(self, mock_bar):
        mock_bar.return_value = 8
        result = app.foo_0(5)
        self.assertEqual(-3, result)

    def test_foo_0_3(self):
        app.bar = Mock()
        app.bar.return_value = 8
        result = app.foo_0(5)
        self.assertEqual(-3, result)

    @patch.object(app, 'bar')
    @patch.object(app, 'something')
    def test_foo_1_0(self,
                     mock_something,
                     mock_bar):
        app.foo_1(14)
        self.assertEqual(mock_bar.call_count, 1)
        mock_bar.assert_called_once_with(14)
        mock_something.assert_not_called()

    @patch.object(app, 'parse_large_file')
    def test_foo_2_0(self, mock_file):
        mock_file.side_effect = MemoryError
        result = app.foo_2('something')
        self.assertEqual('Boom!', result)

    @patch.object(requests, 'get')
    def test_foo_3_0(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'it works'
        result = app.foo_3('http://localhost')
        self.assertEqual('it works', result)

    @patch.object(app, 'bar')
    def test_foo_4_0(self, mock_bar):
        mock_bar.return_value = 11
        self.assertRaises(Exception, lambda: app.foo_4(8))
