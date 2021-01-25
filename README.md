# QR-Authentication-Entry-Exit-System
An entry-exit system based on QR code, which identifies an entree from the database and does not allow duplicity of entries

The database stores USN(ID) values as varchar along with presence variable which determines whether the person is present in the campus or not
presence = 1 (Present in campus)
presence = 0 (Not present in campus)

Entry.py
If the person's ID is present in the database and presence=0, then the person is admitted to the campus and presence is changed to 1

Exit.py
If the person's ID is present in the database and presence=1, then the person is allowed to exit the campus and presence is changed to 0
