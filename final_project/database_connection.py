"""
program: database_connection.py
Author: Kelly Smith
Last day updated: 12/01/19

Program to create a SURS contact database

"""
import datetime
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('Conactdatabase.db')
c = conn.cursor()


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_tables(database):
    sql_create_contact_table = """ CREATE TABLE IF NOT EXISTS contact (
                                        contact id PRIMARY KEY,
                                        contactdate date NOT NULL,
                                        contactmade number NOT NULL,
                                        contactmode text NOT NULL,
                                        personcontacted text NOT NULL,
                                        engagementid number,
                                        notes text NOT NULL,
                                        staff text NOT NULL
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        create_tables(conn, sql_create_contact_table)
    else:
        print("Unable to connect to " + str(database))


def create_contact(conn, contact):
    sql = ''' INSERT INTO contact(contactdate, contactmade, contactmode,personcontacted,engagementid,notes,staff)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, contact)


def select_all_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    return rows, datetime.datetime.now()


if __name__ == '__main__':
    conn = create_connection("Conactdatabase.db")
    with conn:
        contact = ('01/02/19', 'Yes', 'Email', 'Carrie', '', 'Spoke with Carrie about burden study', 'Kelly')
        contact_id = create_contact(conn, contact)
        rows = select_all_contacts(conn)
        for row in rows:
            print(row)
