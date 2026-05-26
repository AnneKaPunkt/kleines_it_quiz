def main():
    print("=== Wilkommen beim IT_Fachbegriffe-Quiz ===")
    print("Teste dein Wissen!\n")

    # Eine Liste, die mehrere Dictionaries (Fragen) beinhaltet
    fragenpool = [
        {
            "text" : "Was bedeutet die Abkürzung 'RAM'?",
            "optionen" : "A) Read Access Memory\nB) Random Access Memory",
            "loesung" : "B"
        },
        {
            "text" : "Welches Protokoll wird für sichere Webseiten genutzt?",
            "optionen" : "A) HTTP\nB) HTTPS ",
            "loesung" : "B"
        },
        {
            "text" : "Was ist Python in der IT-Welt?",
            "optionen" : "A) Eine Programmiersprache\nB) Ein Betriebssystem",
            "loesung" : "A"
        } 
    ]

    # Eine Variable um die Punkte des Spielers zu zählen
    punkte = 0

    # Die For-Schleife läuft jede Frage im Pool nacheinander durch
    for frage in fragenpool:
        print("-- NÄCHSTE FRAGE --")
        print(frage["text"])
        print(frage["optionen"])


    # Eingabe vom Nutzer holen, Leerzeichen entfernen (.strip) und in Großbuchstaben umwandeln (.upper)
        antwort = input("Deine Antwort (A oder B):").strip().upper()

    # Wir prüfen direkt gegen den Wert hinter dem Schlüssel "loesung"
        if antwort == frage["loesung"]:
            print("Yüpppiiieee! Richtig :) + 1 Punkt\n")
            punkte += 1
        else:
            print(f"Nöpedi...nö! Leider falsch. :( Die richtige Antwort ist {frage['loesung']}.\n")

    # Das Endergebnis nach der Schleife anzeigen
        print("=== SPIEL ENDE ===")
        print(f"Du hast {punkte} von {len(fragenpool)} Punkten erreicht!")
        

if __name__ == "__main__":
    main()
