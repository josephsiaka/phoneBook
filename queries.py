CREATE_TABLE = "CREATE TABLE IF NOT EXISTS PHONEBOOK(" \
               "'id' INTEGER," \
               "'firstName' TEXT(10) NOT NULL," \
               "'lastName' TEXT(10) NOT NULL," \
               "'phoneNumber' INTEGER(11) NOT NULL UNIQUE,"\
               "'email' TEXT(50) NOT NULL UNIQUE,"\
               "'address' TEXT(60) NOT NULL,"\
               "PRIMARY KEY('id' AUTOINCREMENT)" \
               ")"


INSERT = "INSERT INTO PHONEBOOK(id, firstName, lastName, phoneNumber, email, address) VALUES(NULL,?, ?, ?, ?, ?)"

FETCH_ALL = "SELECT * FROM PHONEBOOK"

UPDATE = "UPDATE PHONEBOOK SET firstName= ?,lastName= ?,phoneNumber=?, email=?, address=?  where id = ?"

DELETE = "DELETE FROM PHONEBOOK where id = ?"

