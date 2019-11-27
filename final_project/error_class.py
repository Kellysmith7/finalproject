from tkinter import messagebox
class NotAlpha(Exception):
    """program: error_class.py
    Author: Kelly Smith
    Last day updated: 12/01/19

    Program to create a NotAlpha exception if an entry is not alphabetic
    """
    def __init__(self, message=None):
        if message == None:
            message = messagebox.showinfo("Alpha", "Your entry for person contacted must be alphabetic")
        super(NotAlpha, self).__init__(message)

class NotAlphaTwo(Exception):
    """program: error_class.py
    Author: Kelly Smith
    Last day updated: 12/01/19

    Program to create a NotAlpha exception if an entry is not alphabetic
    """
    def __init__(self, message=None):
        if message == None:
            message = messagebox.showinfo("AlphaStaff","Your entry for staff must be alphabetic")
        super(NotAlphaTwo, self).__init__(message)


class Yesno(Exception):
    """program: error_class.py
    Author: Kelly Smith
    Last day updated: 12/01/19

    Program to create a Yesno exception if an entry is not Yes or No
    """
    def __init__(self, message=None):
        if message == None:
            message = messagebox.showinfo("Y/N", "You must enter yes or no in the contact made section")
        super(Yesno, self).__init__(message)


class Dateformat(Exception):
    """program: error_class.py
    Author: Kelly Smith
    Last day updated: 12/01/19

    Program to create a Dateformat exception if a date is not formatted correctly
    """
    def __init__(self, message=None):
        if message == None:
            message = messagebox.showinfo("Date", "Date must be in the mm/dd/yy format")
        super(Dateformat, self).__init__(message)
