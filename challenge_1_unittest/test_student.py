# Unit test for students

import unittest
from student import Studentlist

class TestStudentLists(unittest.TestCase):
    """Test case class"""
    def setUp(self):
            self.mock_stu_dict = {
              "Harry": 37,
              "Berry": 28.5,
              "Tina": 37,
              "Akriti": 41,
              "Harsh": 39
            }
            self.stu_list = Studentlist(self.mock_stu_dict)

    def test_get_second_lowest(self):
        """test the second lowest score"""
        grade = self.stu_list.get_second_lowest()

    def test_get_the_students(self):
        """test a list of student names who get the second lowest score"""
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
