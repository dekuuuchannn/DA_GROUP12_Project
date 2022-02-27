import unittest
import DA_Group12 as prog


class ProjectTest(unittest.TestCase):


    def test_Files(self):
        self.assertEqual(prog.File, 'Project_File.xlsx')

if __name__ == '__main__':
    unittest.main()
