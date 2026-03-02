def simpele_rekenmachine():
    print("Simpele rekenmachine")
    print("Kies een bewerking: +  -  *  /")
    print("Voer minimaal twee getallen in, gescheiden door spaties")

    while True:
        bewerking = input("Bewerking (of 'stop' om te stoppen): ").strip()
        if bewerking == "stop":
            print("Programma gestopt")
            break

        if bewerking not in ["+", "-", "*", "/"]:
            print("Fout: kies +, -, * of /")
            continue

        invoer = input("Voer de getallen in (minimaal twee, gescheiden door spaties): ").strip()

        try:
            getallen = [float(x) for x in invoer.split()]
        except:
            print("Fout: alleen getallen invoeren.")
            continue

        if len(getallen) < 2:
            print("Fout: voer minimaal twee getallen in.")
            continue

        # Berekening uitvoeren
        resultaat = getallen[0]
        for getal in getallen[1:]:
            if bewerking == "+":
                resultaat += getal
            elif bewerking == "-":
                resultaat -= getal
            elif bewerking == "*":
                resultaat *= getal
            elif bewerking == "/":
                if getal == 0:
                    print("Fout: delen door nul kan niet.")
                    break
                resultaat /= getal
        else:
            print("Resultaat:", resultaat)

simpele_rekenmachine()