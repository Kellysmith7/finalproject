import unittest
import sqlite3
from project_code import database_connection
from project_code.error_class import NotAlpha, NotAlphaTwo, Yesno, Dateformat


class MyTestCase(unittest.TestCase):

    def test_createcontact(self):
        conn = sqlite3.connect('Conactdatabase.db')
        contact = ('01/02/19', 'Yes', 'Email', 'Carrie', '', 'Spoke with Carrie about burden study', 'Kelly')
        expected = "<class 'sqlite3.DatabaseError'>"
        actual = database_connection.create_contact(conn, contact)
        self.assertEqual(actual, expected)

    def test_invalid_staff(self):
        with self.assertRaises(Exception):
            NotAlphaTwo(None, "Your entry for person contacted must be alphabetic")

    def test_invalid_client(self):
        with self.assertRaises(Exception):
            NotAlpha('1', '01/01/19', 'Yes', 'Email', 123, 'EID12345', 'Hi', 'Kelly')

    def test_invalid_contactmade(self):
        with self.assertRaises(Exception):
            Yesno('01/01/19', '2', 'Email', 'Carrie', 'EID12345', 'Hi', 'Kelly')

    def test_invalid_date(self):
        with self.assertRaises(Exception):
            Dateformat('01/01/2019', 'Yes', 'Email', 'Carrie', 'EID12345', 'Hi', 'Kelly')


if __name__ == '__main__':
    unittest.main()
