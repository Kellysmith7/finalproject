import unittest
from final_project.database_connection import create_contact
from final_project.project_gui import submit
from final_project.error_class import Yesno, NotAlphaTwo, NotAlpha, Dateformat


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.contact = contact('01/02/19', 'Yes', 'Email', 'Carrie', '', 'Spoke with Carrie about burden study', 'Kelly'

    def tearDown(self):
        del self.contact

    def test_connection(self):
        self.assertEqual(create_contact('01/10/09', 'Yes', 'Email', 'Bob', '', 'Test', 'Kelly'),
                         'New Record Date: 01/10/09 Engaged: Yes Via: Email Client: Bob Engagement ID: N/A Notes: Test Staff: Kelly')

    def staff_error(self):
        self.assertEqual(submit('1', '01/01/19', 'Yes', 'Email', 'Carrie', 'EID12345', 'Hi', '123'),
                         "Your entry for staff must be alphabetic")

    def test_invalid_staff(self):
        with self.assertRaises(Exception):
            NotAlphaTwo(None, "Your entry for person contacted must be alphabetic")

    def test_invalid_client(self):
        with self.assertRaises(Exception):
            NotAlpha('1', '01/01/19', 'Yes', 'Email', 123, 'EID12345', 'Hi', 'Kelly')

    def test_invalid_contactmade(self):
        with self.assertRaises(Exception):
            contact = Yesno('01/01/19', '2', 'Email', 'Carrie', 'EID12345', 'Hi', 'Kelly')

    def test_invalid_date(self):
        with self.assertRaises(Exception):
            Dateformat('01/01/2019')


if __name__ == '__main__':
    unittest.main()
