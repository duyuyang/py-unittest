"""
Given a Physics class of students, stored in a dictionary.
Print the name(s) of any students(s) having the second lowest grade.
"""

class Studentlist(object):

    def __init__(self, stu_dict):
        """initiate the object"""
        self.stu_dict = stu_dict


    def get_second_lowest(self):
        """return the second lowest grade from the given dictionary"""


    def get_the_students(self, second_lowest):
        """return the names of students with second_lowest grade"""


    def main(self):
        """main function here"""



if __name__ == "__main__":
    stu_dict = {
      "Harry": 37,
      "Berry": 28.5,
      "Tina": 37,
      "Akriti": 41,
      "Harsh": 39
    }
    SL = Studentlist(stu_dict)
    SL.main()
