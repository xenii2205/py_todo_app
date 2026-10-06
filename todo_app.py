from pathlib import Path
import json

#import os

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#file_path = os.path.join(BASE_DIR, "todo_data.json")

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "todo_data.json"


# JSON-Datei lesen und Daten zurückgeben
def open_lists():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Datei nicht gefunden. Erstelle eine neue leere Liste.")
        return {"offen": [], "erledigt": []}


# JSON-Datei mit neuen Daten speichern
def save_lists(data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Listen anzeigen
def show_lists(data):
    for status, task_list in data.items():  # .items() für Dictionaries
        print(f"{status}:")
        for task in task_list:
            print(f"- {task}")


# Menü ausgeben
def show_menu():
#    print("Was möchtest du machen?\n _______________________\n Liste Anzeigen\n 2. Eintrag erledigt markieren\n 3. Eintrag hinzufügen\n 4. Eintrag löschen\n 5. Programm beenden\n")
    print("Was möchtest du machen?")
    print("_______________________")
    print("1. Liste Anzeigen")
    print("2. Eintrag erledigt markieren")
    print("3. Eintrag Hinzufügen")
    print("4. Eintrag Löschen")
    print("5. Programm Beenden")
    print("")


# Offene aufgaben drucken
def show_open(data):
    print("Offen")
    for task in data["offen"]:
        print(f"- {task}")


# Erledigte Aufgabe drucken
def show_done(data):
    print("Erledigt")
    for task in data["erledigt"]:
        print(f"- {task}")



def lets_do(data):
    while True:
        # Menü ausgeben
        show_menu()

        # Eingabe abrfagen und ValueError abfangen  
        try:
            choice = int(input("Wähle (z.B. 1): "))
            print("___________________")
        except ValueError:
            print("Bitte gebe eine gültige Zahl ein!")
            continue # Schleife von vorne starten

        # Aktion auswählen
        try:
            if choice == 1:
                show_lists(data)  # Aufgaben anzeigen

            elif choice == 2:  # Aufgabe als erledigt markieren
                if not data["offen"]:
                    print("Keine offenen Aufgaben!\n")
                    continue

                show_open(data)

                aufg = input("Aufgaben Name: ")
                if aufg in data["offen"]:
                    data["offen"].remove(aufg)
                    data["erledigt"].append(aufg)
                    print(f"'{aufg}' wurde als erledigt markiert.\n")
                else:
                    print(f"'{aufg}' nicht in der 'offen'-Liste gefunden.")
                    continue

                show_lists(data)
                input("\nDrücke Enter, um zum Menü zurückzukehren...")

            elif choice == 3:  # Aufgabe hinzufügen
                aufg = input("Aufgaben Name: ")
                data["offen"].append(aufg)
                print(f"'{aufg}' wurde hinzugefügt.\n")
                show_open(data)
                input("\nDrücke Enter, um zum Menü zurückzukehren...")

            elif choice == 4:  # Aufgabe löschen
                aufg = input("Aufgaben Name: ")   

                if aufg in data["offen"]:
                    data["offen"].remove(aufg)
                    print(f"'{aufg}' wurde aus 'offen' gelöscht.\n")   
                elif aufg in data["erledigt"]:
                    data["erledigt"].remove(aufg)
                    print(f"'{aufg}' wurde aus 'erledigt' gelöscht.\n")
                else:
                    print(f"'{aufg}' nicht gefunden.\n")
                    continue
               
                show_lists(data)
                input("\nDrücke Enter, um zum Menü zurückzukehren...")

            elif choice == 5: # Schleife beenden
                save_lists(data)  # Änderungen speichern               
                print("Programm beendet")
                break
            
            else:
                print("Ungültige Auswahl. Bitte wähle 1, 2, 3, 4. oder 5.\n")
        
        except Exception as e:
            print(f"Fehler: {e}\n")
            continue    



data = open_lists()  # Daten laden
lets_do(data)  # Funktion aufrufen




