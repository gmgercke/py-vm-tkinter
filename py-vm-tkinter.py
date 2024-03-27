import os
import random
import tkinter as tk
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

# Funktion: Button: Nutzer gibt ein, welches Getränk er möchte.
# Wenn das Getränk in der "drinks" Liste existiert geht es unten weiter.
# Wenn das Getränk in der Liste nicht existiert, ended das Programm mit einer Fehlermeldung.


auswahl = tk.Label(window)
error = tk.Label(window)
bezahl = tk.Label(window)
surprise = tk.Label(window)


def submit():
    choiceSet = varChoice.get()
    varChoice.set("")
    numberSet = (varNumber.get())
    varNumber.set("")

    global auswahl
    global error
    global bezahl
    global surprise

    auswahl.destroy()
    error.destroy()
    bezahl.destroy()
    surprise.destroy()

    found = False
    rando = random.choice(drinks)

    for x in drinks:
        if choiceSet.lower() == x.lower() or choiceSet.lower() == "Überraschung".lower():
            auswahl_text = f"\nDu hast {numberSet}x {choiceSet.capitalize()} gewählt."
            auswahl = tk.Label(text=auswahl_text, font=mainFont)
            auswahl.grid()
            found = True
            break

    if not found:
        error_text = f"\n{choiceSet.capitalize()} ist keine gültige Eingabe. Bitte versuche es noch einmal."
        error = tk.Label(text=error_text, font=mainFont)
        error.grid()
        return

    # Nutzer gibt die Anzahl des Getränkes ein, das er möchte.
    # Die Schleife stopt in beiden Listen (drinks, prices), sobald der erste Treffer gelandet ist.
    # Dannach wird die angegebene Menge mit dem Listenpreis multipliziert und ausgegeben.

    numberSet = int(numberSet)
    for x, y in zip(drinks, prices):
        if choiceSet.lower() == x.lower():
            bezahl_text = f"""\n{numberSet} {choiceSet.capitalize()} kosten insgesamt {numberSet*y:.2f} €.\n\nMöchtest du bar zahlen oder mit Karte?"""
            bezahl = tk.Label(text=bezahl_text, font=mainFont)
            bezahl.grid()
            break

        elif choiceSet.lower() == "Überraschung".lower():
            for a, b in zip(drinks, prices):
                if rando == a:
                    surprise_text = f"""Es wurde {rando.capitalize()} für dich ausgewählt. {numberSet} {rando.capitalize()} kosten insgesamt {numberSet*b:.2f} €.\n\nMöchtest du bar zahlen oder mit Karte?"""
                    surprise = tk.Label(text=surprise_text, font=mainFont)
                    surprise.grid()
                    break

                elif rando == "Gummibärchen".lower():
                    surprise_text = f"""Überraschung! Du bekommst eine Tüte {rando.capitalize()}. Das kostet dich nichts! Viel Spaß damit!"""
                    surprise = tk.Label(text=surprise_text, font=mainFont)
                    surprise.grid()
                    break


numberSet = varNumber.get()
choiceSet = varChoice.get()
choice = tk.Label(text="Deine Wahl: ", font=mainFont)
choice.grid()

# Vorschautext in Eingabefeldern werden definiert und an das Reinklicken ins Feld gebunden

choiceEntry = (tk.Entry(textvariable=varChoice))
choiceEntry.grid()
choiceEntry.insert(0, "Getränk")
choiceEntry.configure(state="disabled")

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

window.mainloop()
