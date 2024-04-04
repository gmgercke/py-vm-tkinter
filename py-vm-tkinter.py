import os
import random
import tkinter as tk
from tkinter import ttk
import tkinter.font

# Definition des tkinter Fensters und Überschrift, sowie verschiedenen Fonts
window = tk.Tk()
window.title("Getränkeautomat")
window.config(border=25)
greetingFont = tkinter.font.Font(family="Helvetica", size=16, weight="bold")
mainFont = tkinter.font.Font(family="Helvetica", size=12)
greeting = tk.Label(text="Willkommen bei Trink-O-Mat!", font=greetingFont)
greeting.grid()


# Zuerst definiere ich das Objekt "Drink", das einen Namen und einen Preis bekommt
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price


d1 = Drink("Kaffee", 1.50)
d2 = Drink("Tee", 1.35)
d3 = Drink("Kakao", 2.10)
d4 = Drink("Wasser", 0.75)
d5 = Drink("Gummibärchen", 0.00)

# Hier packe ich die Namen und Preise der Objekte in Listen, um sie später einfacher durchsuchen zu können
drinks = [d1.name, d2.name, d3.name, d4.name, d5.name]
prices = [d1.price, d2.price, d3.price, d4.price, d5.price]

drinklist_text = (f"""\nHallo {os.getlogin()}, es stehen folgende Getränke zur Auswahl:\n
        {d1.name} für {d1.price:.2f} €
        {d2.name} für {d2.price:.2f} €
        {d3.name} für {d3.price:.2f} €
        {d4.name} für {d4.price:.2f} €
        Gib 'Überraschung' für eine Zufallsauswahl ein! \n""")

drinklist = tk.Label(text=drinklist_text, anchor="w", justify="left", font=mainFont)
drinklist.grid()

varChoice = tk.StringVar()
varNumber = tk.StringVar()


# Funktion: Vorschautext in Eingabefeld verschwindet beim Reinklicken
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


# Funktion: Vorschautext in Eingabefeld kehrt zurück beim Rausklicken
def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


# Labels werden als existent vordefiniert, um sie später ausserhalb der Schleife manipulieren zu können
auswahl = tk.Label(window)
error = tk.Label(window)
bezahl = tk.Label(window)
surprise = tk.Label(window)
gsurprise = tk.Label(window)

# Funktion: Button: Nutzer gibt ein, welches Getränk und wieviel davon er möchte, klickt dann Bestellen
def submit():
    # Die Variablen für Auswahl und Menge werden als "leer" vordefiniert
    choiceSet = choiceEntry.get()
    varChoice.set("")
    numberSet = varNumber.get()
    varNumber.set("")

    # Die Variablen werden als global vordefiniert, um sie ausserhalb der Schleife manipulieren zu können
    global auswahl
    global error
    global bezahl
    global surprise
    global gsurprise

    # Die Label werden bei Knopfdruck, aber vorm Erstellen des neuen Labels, gelöscht
    auswahl.destroy()
    error.destroy()
    bezahl.destroy()
    surprise.destroy()
    gsurprise.destroy()

    # found als Hilfsvariable, um Existenz eines Listeneintrags zu bestätigen
    found = False
    # Erstellung einer Zufallsauswahl für die Eingabemöglichkeit "Überraschung"
    rando = random.choice(drinks)

    # Eingabe wird mit Drink-Liste abgeglichen
    # Wenn Übereinstimmung gefunden, dann wird die Bestellung bestätigt
    for x in drinks:
        if choiceSet.lower() == x.lower() or choiceSet.lower() == "Überraschung".lower():
            auswahl_text = f"\nDu hast {numberSet}x {choiceSet.capitalize()} gewählt."
            auswahl = tk.Label(text=auswahl_text, font=mainFont)
            auswahl.grid()
            found = True
            break

    # Wenn nicht gefunden, gib eine Fehlermeldung aus
    if not found:
        error_text = f"\n{choiceSet.capitalize()} ist keine gültige Eingabe. Bitte versuche es noch einmal."
        error = tk.Label(text=error_text, font=mainFont)
        error.grid()
        return

    # die angegebene Anzahl wird sicherheitshalber als int definiert
    numberSet = int(numberSet)

    # Beide Listen (Drinks, Preise) werden durchsucht
    # In beiden Listen wird gestoppt, sobald der erste Treffer gefunden wurde
    # Die bestellte Menge wird mit dem Listenpreis multipliziert
    # Bestellung mit Gesamtpreis wird ausgegeben
    for x, y in zip(drinks, prices):
        if choiceSet.lower() == x.lower():
            bezahl_text = f"""\n{numberSet} {choiceSet.capitalize()} kosten insgesamt {numberSet*y:.2f} €.\n\nMöchtest du bar zahlen oder mit Karte?"""
            bezahl = tk.Label(text=bezahl_text, font=mainFont)
            bezahl.grid()
            break
        # Das Gleiche, wenn die Eingabe "Überraschung" war
        elif choiceSet.lower() == "Überraschung".lower():
            if rando == x and rando != "Gummibärchen":
                surprise_text = f"""Es wurde {rando.capitalize()} für dich ausgewählt. {numberSet} {rando.capitalize()} kosten insgesamt {numberSet*y:.2f} €.\n\nMöchtest du bar zahlen oder mit Karte?"""
                surprise = tk.Label(text=surprise_text, font=mainFont)
                surprise.grid()

            # Die Wahl "Überraschung" hat auch die Chance, gratis Gummibärchen auszuspucken
            elif rando == "Gummibärchen":
                gsurprise_text = f"""Überraschung! Du bekommst eine Tüte {rando.capitalize()}. Das kostet dich nichts! Viel Spaß damit!"""
                gsurprise = tk.Label(text=gsurprise_text, font=mainFont)
                gsurprise.grid()
                break


choice = tk.Label(text="Deine Wahl: ", font=mainFont)
choice.grid()


# def divide_drinks():
#     for item in drinks:
#         yield item
#

#for value in divide_drinks():
    

# Vorschautext in Eingabefeldern werden definiert und an das Reinklicken ins Feld gebunden
choiceEntry = ttk.Combobox(values=["Kaffee", "Tee", "Wasser", "Kakao", "Überraschung"])
choiceEntry.grid()
choiceEntry.insert(0, " ")
#choiceEntry.configure(state="disabled")

button = ttk.Button(text="Auswahl", command=submit)

numberEntry = tk.Entry(textvariable=varNumber)
numberEntry.grid()
numberEntry.insert(0, "Anzahl")
numberEntry.configure(state="disabled")

choice_focus_in = choiceEntry.bind('<Button-1>', lambda x: on_focus_in(choiceEntry))
choice_focus_out = choiceEntry.bind(
    '<FocusOut>', lambda x: on_focus_out(choiceEntry, "Getränk"))

number_focus_in = numberEntry.bind('<Button-1>', lambda x: on_focus_in(numberEntry))
number_focus_out = numberEntry.bind(
    '<FocusOut>', lambda x: on_focus_out(numberEntry, "Anzahl"))

# Bestellbutton

choiceButton = tk.Button(text="Bestellen", command=submit)
choiceButton.grid()

# das TKinter Fenster mit allen oben festgelegten Inhalten wird initialisiert

window.mainloop()
