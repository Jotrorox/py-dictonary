import database as db
import prompts as pr

MENU_PROMPT = """
--- Wörter Datenbank App ---
Bitte wähle eine option:
1) Füge ein neues Wort hinzu
2) Zeige Alle Wörter
3) Suche nach einem Wort
4) Editiere ein Wort mit der ID
5) Lösche ein Wort mit der ID
9) EXIT
Deine Wahl: """

def menu():

    connection = db.connect()

    db.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "9":

        if user_input == "1":

            pr.prompt_add_word()

        elif user_input == "2":

            pr.prompt_show_words()

        elif user_input == "3":

           pr.prompt_search_word_by_eng()

        elif user_input == "4":

            pr.prompt_edit_word_by_id()

        elif user_input == "5":

            pr.delete_word_by_id()

        else:

            print("Unerwartete/Falsche eingabe, bitte versuche es erneut!")

menu()