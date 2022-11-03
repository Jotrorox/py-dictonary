import sqlite3 as sq

CREATE_WORDS_TABLE = 'CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY, english TEXT, german TEXT);'

INSERT_WORD = 'INSERT INTO words (english, german) VALUES (?, ?);'

GET_ALL_WORDS = 'SELECT * FROM words;'

GET_WORD_BY_NAME = 'SELECT * FROM words WHERE english = ?'

EDIT_ENGLISH_BY_ID = 'UPDATE words SET english = ? WHERE ID = ?;'
EDIT_GERMAN_BY_ID = 'UPDATE words SET german = ? WHERE ID = ?;'

DELETE_WORD_BY_ID = 'DELETE FROM words WHERE id = ?;'

def connect():

    return sq.connect('data.db')

def create_tables(connection):

    with connection:
        connection.execute(CREATE_WORDS_TABLE)

def add_word(connection, eng, ger):

    with connection:
        connection.execute(INSERT_WORD, (eng, ger))

def get_all_words(connection):

    with connection:
        return connection.execute(GET_ALL_WORDS).fetchall()

def get_word_by_eng(connection, name):

    with connection:
        return connection.execute(GET_WORD_BY_NAME, (name,)).fetchall()

def edit_word_by_id(connection, ID, thing_to_edit, new_version):

    try: 
    
        if thing_to_edit == "english":

            with connection:
                return connection.execute(EDIT_ENGLISH_BY_ID, (new_version, ID))

        elif thing_to_edit == "german":

            with connection:
                return connection.execute(EDIT_GERMAN_BY_ID, (new_version, ID))

        else: 

            print("Falsches Argument!")

    except:

        print("Da ist etwas schiefgelaufen, versuche es bitte nochmal!")

def delete_word_by_id(connection, ID):

    try:

        with connection:
            return connection.execute(DELETE_WORD_BY_ID, (ID))

    except:

        print("Da ist etwas schiefgelaufen, versuche es bitte nochmal!")