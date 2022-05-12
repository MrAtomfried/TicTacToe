import random

def spielfeld_anzeigen(spielfeld):
    """ Zeige das aktuelle Spielfeld im Terminal an. """

    print("\n" * 100)
    print('   |   |')
    print(' ' + spielfeld[7] + ' | ' + spielfeld[8] + ' | ' + spielfeld[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + spielfeld[4] + ' | ' + spielfeld[5] + ' | ' + spielfeld[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + spielfeld[1] + ' | ' + spielfeld[2] + ' | ' + spielfeld[3])
    print('   |   |')

def markierung_setzen(spielfeld, markierung, position):
    """ Setzt die markierung im spielfeld am Index position. """

    spielfeld[position] = markierung

def sieg_check(spielfeld, markierung):
    """ Gibt True zurück, wenn markierung im aktuellen spielfeld gewinnt. """

    return ((spielfeld[7] == markierung and spielfeld[8] == markierung and spielfeld[9] == markierung) or  # oben
            # mitte
            (spielfeld[4] == markierung and spielfeld[5] == markierung and spielfeld[6] == markierung) or
            # unten
            (spielfeld[1] == markierung and spielfeld[2] == markierung and spielfeld[3] == markierung) or
            # linke seite runter
            (spielfeld[7] == markierung and spielfeld[4] == markierung and spielfeld[1] == markierung) or
            # mitte runter
            (spielfeld[8] == markierung and spielfeld[5] == markierung and spielfeld[2] == markierung) or
            # rechte seite runter
            (spielfeld[9] == markierung and spielfeld[6] == markierung and spielfeld[3] == markierung) or
            # diagonal
            (spielfeld[7] == markierung and spielfeld[5] == markierung and spielfeld[3] == markierung) or
            (spielfeld[9] == markierung and spielfeld[5] == markierung and spielfeld[1] == markierung))  # diagonal

def spieler_eingabe():
    """ Erwartet vom Spieler die Eingabe 'X' oder 'O' und gibt diese zurück. """

    markierung = ''

    while not (markierung == 'X' or markierung == 'O'):
        markierung = input('Spieler 1: Willst du X oder O sein?').upper()

    if markierung == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def erster_spieler():
    """ Gibt einen String zurück, der einem zufällig ausgewählten Spieler entspricht. """

    if random.randint(0, 1) == 0:
        return 'Spieler 2'
    else:
        return 'Spieler 1'

def spielfeldwahl():
    field = int(input("Wählen Sie eine Zahl zwischen 1 und 9 aus: "))
    if field is not range(1, 10):
        print("Falsche Eingabe!")

def spieler_wahl(spielfeld):
    """ Erfragt vom Spieler den nächsten Zug, stellt sicher,
    dass diese Position noch frei ist und gibt sie zurück.
    """

    position = 0

    while position not in range(1, 10) or not platz_check(spielfeld, int(position)):
        position = int(input('Wähle deine nächste Position: (1-9) '))

    return position


def platz_check(spielfeld, position):
    """ Überprüft, ob das Feld am Index position im spielfeld frei ist
    und gibt einen entsprechenden bool'schen Wert zurück.
    """

    return spielfeld[position] == ' '

def spielfeld_voll(spielfeld):
    """ Gibt True zurück, wenn das spielfeld voll ist, und ansonsten False. """

    for i in range(1, 10):
        if platz_check(spielfeld, i):
            return False

    return True

def neues_spiel():
    """ Fragt die Spieler, ob sie ein weiteres Spiel wünschen und
    gibt einen entsprechenden bool'schen Wert zurück.
    """

    return input('Wollt ihr erneut spielen? Gebt Ja oder Nein ein: ').lower().startswith('j')

print("Willkommen bei TicTacToe!")

while True:

    # Das Spielfeld zurücksetzen
    das_feld = [' '] * 10
    spieler1_markierung, spieler2_markierung = spieler_eingabe()
    zug = erster_spieler()
    print(zug + " darf beginnen.")

    spielen = input('Bist du bereit zum spielen? Gib Ja oder Nein ein.')

    if spielen.lower()[0] == 'j':
        spiel_laeuft = True
    else:
        spiel_laeuft = False

    while spiel_laeuft:
        if zug == "Spieler 1":
            # Zug von Spieler 1

            spielfeld_anzeigen(das_feld)
            position = spieler_wahl(das_feld)
            markierung_setzen(das_feld, spieler1_markierung, position)

            if sieg_check(das_feld, spieler1_markierung):
                spielfeld_anzeigen(das_feld)
                print("Glückwunsch! Du hast gewonnen!")
                spiel_laeuft = False
            else:
                if spielfeld_voll(das_feld):
                    spielfeld_anzeigen(das_feld)
                    print("Dieses Spiel ist ein Unentschieden!")
                    break
                else:
                    zug = "Spieler 2"
        else:
            # Zug von Spieler 2

            spielfeld_anzeigen(das_feld)
            position = spieler_wahl(das_feld)
            markierung_setzen(das_feld, spieler2_markierung, position)

            if sieg_check(das_feld, spieler2_markierung):
                spielfeld_anzeigen(das_feld)
                print("Glückwunsch! Du hast gewonnen!")
                spiel_laeuft = False
            else:
                if spielfeld_voll(das_feld):
                    spielfeld_anzeigen(das_feld)
                    print("Dieses Spiel ist ein Unentschieden!")
                    break
                else:
                    zug = "Spieler 1"

    if not neues_spiel():
        break