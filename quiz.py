def main():
    print("=== Wilkommen beim IT_Fachbegriffe-Quiz ===")
    print("Teste dein Wissen!\n")

    # Ein Wörterbuch (Dictionary) für die Frage erstellen
    frage_data = {
        "text" : "Was bedeutet die Abkürzung 'RAM'?",
        "optionen" : "A) Read Access Memory\nB) Random Access Memory",
        "loesung" : "B"
    } 

    # Die Daten aus dem Dictionary über die Schlüssel (Keys) anzeigen
    print(frage_data["text"])
    print(frage_data["optionen"])

    # # Eine Frage auf dem Bildschirm anzeigen
    # print("Frage 1: Was bedeutet die Abkürzung 'RAM'?")
    # print("A) Read Access Memory\nB) Random Access Memory")

    # Eingabe vom Nutzer holen, Leerzeichen entfernen (.strip) und in Großbuchstaben umwandeln (.upper)
    antwort = input("Deine Antwort (A oder B):").strip().upper()

    # Die Antwort überprüfen
    # if antwort == "B":
    #     print("Yüpppiiieee! Richtig :) RAM steht für Random Access Memory")
    # else:
    #     print("Nöpedi...nö! Leider falsch :( RAM steht für Random Access Memory")

    # Wir prüfen direkt gegen den Wert hinter dem Schlüssel "loesung"

    if antwort == frage_data["loesung"]:
        print("Yüpppiiieee! Richtig :) RAM steht für Random Access Memory")
    else:
         print(f"Nöpedi...nö! Leider falsch. :( Die richtige Antwort ist {frage_data['loesung']} (Random Access Memory).")
        


if __name__ == "__main__":
    main()
