import database as db

connection = db.connect()

def prompt_add_word():

    eng = input("Englisch: ")
    ger = input("Deutsch: ")

    db.add_word(connection, eng, ger)

def prompt_show_words():
    
    words = db.get_all_words(connection)

    for word in words: 

        print(f"ID: {word[0]} | {word[1]} <-> {word[2]}")

def prompt_search_word_by_eng():

    eng = input("Englisches Wort: ")

    words = db.get_word_by_eng(connection, eng)

    for word in words: 

        print(f"ID: {word[0]} | {word[1]} <-> {word[2]}")

def prompt_edit_word_by_id():

    id = input("ID des Wortes das du editieren willst: ")
    thing_to_edit = input("Was willst du editieren (english, german): ")
    new_version = input("Das neue Wort: ")

    db.edit_word_by_id(connection, id, thing_to_edit, new_version)

def delete_word_by_id():

    id = input("ID des Wortes das du löschen willst: ")

    db.delete_person_by_id(connection, id)