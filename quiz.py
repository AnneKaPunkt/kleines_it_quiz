def main():
    print("=== Wilkommen beim IT_Fachbegriffe-Quiz ===")
    print("Teste dein Wissen!\n")

    # Eine Frage auf dem Bildschirm anzeigen
    print("Frage 1: Was bedeutet die Abkürzung 'RAM'?")
    print("A) Read Access Memory\nB) Random Access Memory")

    # Eingabe vom Nutzer holen, Leerzeichen entfernen (.strip) und in Großbuchstaben umwandeln (.upper)
    antwort = input("Deine Antwort (A oder B):").strip().upper()

    # Die Antwort überprüfen
    if antwort == "B":
        print("Yüpppiiieee! Richtig :) RAM steht für Random Access Memory")
    else:
        print("Nöpedi...nö! Leider falsch :( RAM steht für Random Access Memory")


if __name__ == "__main__":
    main()
