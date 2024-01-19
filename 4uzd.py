def lasit_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(f"Faila saturs:\n{saturs}")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Nezināma kļūda: {e}")

# Lietotāja ievade
faila_nosaukums = input("Ievadi faila nosaukumu: ")
formāts = input("Ievadi faila formātu (paplašinājumu): ")

if not formāts.startswith("."):
    formāts = "." + formāts

atļautie_formāti = [".txt", ".csv", ".json"]
if formāts not in atļautie_formāti:
    print(f"Kļūda: Nepieļaujamais faila formāts '{formāts}'. Atļautie formāti ir {', '.join(atļautie_formāti)}.")
else:
    lasit_failu(faila_nosaukums)

