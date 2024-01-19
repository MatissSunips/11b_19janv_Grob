vards = input("Ievadi savu vārdu: ")

try:
    with open("vards.txt", "w") as xd:
        xd.write(vards)
except (FileExistsError, ValueError):
    print("Error: Fails jau eksistē vai ievade nav derīga!")
with open("vards.txt", "r") as f:
    name = f.read()

print("Čau mans mīļais, " + vards + "!!!!")
